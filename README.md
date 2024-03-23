# JSD-Tim1

## Fullstack (.fs)

<b>Fullstack</b> is a domain-specific language (DSL)  for generating SpringBoot and Angular projects with CRUD operations of given entity models and REST paths. 

The file extension for your model must be .fs.

## Grammar
[TODO]

## Instructions

To generate SpringBoot application use following command:
```
textx generate [PATH TO .fs FILE] --target springboot -o example/example_output --overwrite
```

To generate Angular application use following command:
```
textx generate [PATH TO .fs FILE] --target angular -o example/example_output --overwrite
```

Main difference between previous two commands is `--target` parameter, which can take values
<i>springboot</i> or <i>angular</i> whether you're generating frontend or backend application.

Example usage:
<code>
textx generate example/userExample.fs --target springboot -o example/example_output --overwrite
</code>


## Example 
[TODO]

# Credits

Initial project layout generated with `textx startproject`.