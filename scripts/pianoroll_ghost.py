from dolphin import event
import csv
import math
from framesequence import FrameSequence
import mkw_core as core
import mkw_classes as classes


@event.on_savestateload
def onSavestateLoad(is_slot, slot):
    controller = classes.GhostController(1)
    sequence = FrameSequence(r'filepath')
    prev_button_mask = 0

    for frame in sequence.frames:
        curr_button_mask = controller.face_button_stream.mask_buttons(
            frame.accel, frame.brake, frame.item, prev_button_mask)
        controller.face_button_stream.write_frame(curr_button_mask)

        stick_mask = controller.stick_input_stream.mask_stick(
            frame.stick_x, frame.stick_y)
        controller.stick_input_stream.write_frame(stick_mask)

        dpad_mask = controller.direction_button_stream.mask_dpad(
            frame.dpad_up, frame.dpad_down, frame.dpad_left, frame.dpad_right)
        controller.direction_button_stream.write_frame(dpad_mask)

        prev_button_mask = curr_button_mask
