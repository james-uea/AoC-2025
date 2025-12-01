def wrap_to_zero(dial_pos):
    if dial_pos > 99:
        # Anything over 99 wraps back around to 0
        dial_pos = dial_pos - 100
        dial_pos = wrap_to_zero(dial_pos)
        pass
    elif dial_pos < 0:
        # Anything under 0 wraps around to 99
        dial_pos = 100 + dial_pos
        dial_pos = wrap_to_zero(dial_pos)
        pass

    return dial_pos

def apply_rotations(dial_pos, rotations, zero_count=0):
    for rotation in rotations:
        if dial_pos > 99 or dial_pos < 0:
            dial_pos = wrap_to_zero(dial_pos)

        # print(dial_pos, rotations, zero_count)
            
        if dial_pos == 0:
            zero_count += 1
        
        shift_type, shift_distance = rotation[0], int(rotation[1:])
        # print(shift_type, shift_distance)

        if shift_type == "L":
            dial_pos -= shift_distance
        else:
            dial_pos += shift_distance

    if dial_pos > 99 or dial_pos < 0:
        dial_pos = wrap_to_zero(dial_pos)

    return dial_pos, zero_count

def main():
    # with open("day1/sample.txt", "r") as r:
    #     p_input = r.readlines()
    # p_input = [line.strip() for line in p_input]

    # dial_pos = 50
    # dial_pos, zero_count = apply_rotations(dial_pos, p_input)

    # print(dial_pos, zero_count)
    with open("day1/input.txt", "r") as r:
        p_input = r.readlines()
    p_input = [line.strip() for line in p_input]

    dial_pos = 50
    dial_pos, zero_count = apply_rotations(dial_pos, p_input)

    print(dial_pos, zero_count)


if __name__ == "__main__":
    main()