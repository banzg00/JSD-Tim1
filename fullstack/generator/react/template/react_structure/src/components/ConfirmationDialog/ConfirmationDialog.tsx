import React from 'react';
import { Dialog, DialogActions, DialogTitle, Button } from '@mui/material';

interface ConfirmationDialogProps {
  open: boolean;
  onClose: (confirmed: boolean) => void;
}

const ConfirmationDialog: React.FC<ConfirmationDialogProps> = ({ open, onClose }) => {
  const handleCancel = () => {
    onClose(false);
  };

  const handleConfirm = () => {
    onClose(true);
  };

  return (
    <Dialog open={open} onClose={() => onClose(false)}>
      <div className="flex flex-col gap-y-4 px-10 py-4 rounded-xl">
        <DialogTitle>Are you sure you want to delete this?</DialogTitle>
        <DialogActions className="flex gap-x-4 items-center" align="center">
          <Button onClick={handleCancel} variant="outlined" color="primary" className="w-[8vw]">Cancel</Button>
          <Button onClick={handleConfirm} variant="contained" color="secondary" className="w-[8vw]">Delete</Button>
        </DialogActions>
      </div>
    </Dialog>
  );
};

export default ConfirmationDialog;
