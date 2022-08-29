#!/usr/bin/python3
import argparse

parser = argparse.ArgumentParser(description='DTM splitter used for AGDQ 2023')
parser.add_argument('--file', '-f', help='DTM file',
                    default=2)
args = parser.parse_args()

with open(args.file, "rb") as f:
    buffer = f.read()
    header_buffer = buffer[:0x100]
    buffer = buffer[0x100:]
    original_buffer = buffer

segment_start_marker = []
segment_end_marker = []
for i in range(len(buffer) // 8):
    pad = buffer[:0x8]
    buffer = buffer[0x8:]
    # Segment start marker
    if (pad[1] & 0x02):
        print("start", pad, i)
        segment_start_marker.append(i-142)
    # Segment start marker
    if (pad[1] & 0x01):
        print("end", pad, i)
        segment_end_marker.append(i)

# print(segment_start_marker)
# print(segment_end_marker)

is_start = False
start_frame = 0
segment_buffer = None
segment_count = 1
for i in range(len(original_buffer) // 8):
    if i in segment_start_marker:
        if not is_start:
            # start recording
            start_frame = i
            print("hit start", i)
            is_start = True
    if i in segment_end_marker:
        if is_start:
            # stop recording
            print("hit end", i)
            segment_buffer = original_buffer[start_frame*8:i*8]
            is_start = False
            print(len(segment_buffer))
            with open("segment_" + str(segment_count) + ".dtm", "wb") as f:
                f.write(header_buffer)
                f.write(segment_buffer)
            segment_count += 1
