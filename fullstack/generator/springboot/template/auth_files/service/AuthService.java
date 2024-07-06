package uns.ac.rs.uks.service;

import org.apache.commons.lang3.RandomStringUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.BadCredentialsException;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;
import uns.ac.rs.uks.dto.request.LoginRequest;
import uns.ac.rs.uks.dto.request.PasswordResetRequest;
import uns.ac.rs.uks.dto.request.PasswordUpdateRequest;
import uns.ac.rs.uks.dto.request.RegistrationRequest;
import uns.ac.rs.uks.dto.response.TokenResponse;
import uns.ac.rs.uks.dto.response.UserDTO;
import uns.ac.rs.uks.exception.AlreadyExistsException;
import uns.ac.rs.uks.exception.NotAllowedException;
import uns.ac.rs.uks.exception.NotFoundException;
import uns.ac.rs.uks.mapper.UserMapper;
import uns.ac.rs.uks.model.RoleEnum;
import uns.ac.rs.uks.model.User;
import uns.ac.rs.uks.security.TokenProvider;
import uns.ac.rs.uks.util.EncryptionUtil;

import java.util.Base64;
import java.util.Random;


@Service
public class AuthService {

    @Autowired
    private AuthenticationManager authenticationManager;

    @Autowired
    private TokenProvider tokenProvider;

    @Autowired
    private UserService userService;

    @Autowired
    private RoleService roleService;

    @Autowired
    private PasswordEncoder passwordEncoder;

    @Autowired
    private EmailService emailService;

    public UserDTO register(RegistrationRequest registrationRequest) throws AlreadyExistsException, NotFoundException{
        if (userService.existsByEmail(registrationRequest.getEmail()))
            throw new AlreadyExistsException("User already exists!");

        User user = UserMapper.toUserFromRequest(registrationRequest);
        String password = EncryptionUtil.decodeBase64(registrationRequest.getPassword());
        user.setPassword(passwordEncoder.encode(password));
        user.setRole(roleService.getRoleByName(RoleEnum.ROLE_USER.getName()));
        User savedUser = userService.save(user);
        return UserMapper.toDTO(savedUser);
    }

    private String generateRandomNumbers() {
        Random random = new Random();
        int randomNumber = random.nextInt(9000) + 1000;
        return String.valueOf(randomNumber);
    }

    public TokenResponse login(LoginRequest loginRequest) throws NotFoundException {
        if(!isUserAccountValid(loginRequest.getEmail())){
            throw new NotFoundException("User not found!");
        }
        TokenResponse token = authenticateRequest(loginRequest);
        return token;
    }

    private TokenResponse authenticateRequest(LoginRequest loginRequest) throws BadCredentialsException {
        Authentication authentication = authenticationManager.authenticate(new UsernamePasswordAuthenticationToken(
                loginRequest.getEmail(),
                new String(Base64.getDecoder().decode(loginRequest.getPassword()))
        ));
        SecurityContextHolder.getContext().setAuthentication(authentication);

        return createToken(authentication);
    }

    private TokenResponse createToken(Authentication authentication) {
        String accessToken = tokenProvider.generateToken(authentication);
        Long expiresAt = tokenProvider.getExpirationDateFromToken(accessToken).getTime();

        return new TokenResponse(accessToken, expiresAt);
    }

    private boolean isUserAccountValid(String email) {
        User user = userService.getUserByEmail(email);
        return !user.getBlockedByAdmin() && !user.getDeleted();
    }

}