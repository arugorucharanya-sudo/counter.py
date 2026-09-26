# Digital Counter Calculator
# Electrical Engineering / Digital Circuits
#
# Features:
# 1. Up Counter
# 2. Down Counter
# 3. Up/Down Counter
# 4. Binary Counter
# 5. Decade Counter
# 6. Mod-N Counter
# 7. Frequency Division


def decimal_to_binary(number, bits):
    """Convert decimal number to fixed-width binary."""
    return format(number, f"0{bits}b")


def up_counter():
    print("\n========== UP COUNTER ==========")

    bits = int(input("Enter number of bits: "))
    pulses = int(input("Enter number of clock pulses: "))

    if bits <= 0 or pulses < 0:
        print("Enter valid positive values.")
        return

    maximum = (2 ** bits) - 1

    print("\nClock\tBinary\tDecimal")

    for clock in range(pulses + 1):
        count = clock % (maximum + 1)
        binary = decimal_to_binary(count, bits)

        print(f"{clock}\t{binary}\t{count}")


def down_counter():
    print("\n========== DOWN COUNTER ==========")

    bits = int(input("Enter number of bits: "))
    pulses = int(input("Enter number of clock pulses: "))

    if bits <= 0 or pulses < 0:
        print("Enter valid positive values.")
        return

    maximum = (2 ** bits) - 1

    print("\nClock\tBinary\tDecimal")

    for clock in range(pulses + 1):
        count = (maximum - clock) % (maximum + 1)
        binary = decimal_to_binary(count, bits)

        print(f"{clock}\t{binary}\t{count}")


def up_down_counter():
    print("\n========== UP/DOWN COUNTER ==========")

    bits = int(input("Enter number of bits: "))
    pulses = int(input("Enter number of clock pulses: "))
    direction = input("Enter direction (up/down): ").lower()

    if bits <= 0 or pulses < 0:
        print("Enter valid positive values.")
        return

    if direction not in ["up", "down"]:
        print("Enter either 'up' or 'down'.")
        return

    maximum = (2 ** bits) - 1

    print("\nClock\tBinary\tDecimal")

    for clock in range(pulses + 1):

        if direction == "up":
            count = clock % (maximum + 1)
        else:
            count = (maximum - clock) % (maximum + 1)

        binary = decimal_to_binary(count, bits)

        print(f"{clock}\t{binary}\t{count}")


def decade_counter():
    print("\n========== DECADE COUNTER ==========")

    pulses = int(input("Enter number of clock pulses: "))

    if pulses < 0:
        print("Enter a valid number of pulses.")
        return

    print("\nClock\tBinary\tDecimal")

    for clock in range(pulses + 1):
        count = clock % 10
        binary = decimal_to_binary(count, 4)

        print(f"{clock}\t{binary}\t{count}")


def mod_n_counter():
    print("\n========== MOD-N COUNTER ==========")

    mod_value = int(input("Enter MOD value: "))
    pulses = int(input("Enter number of clock pulses: "))

    if mod_value <= 0 or pulses < 0:
        print("Enter valid values.")
        return

    bits = max(1, (mod_value - 1).bit_length())

    print("\nClock\tBinary\tDecimal")

    for clock in range(pulses + 1):
        count = clock % mod_value
        binary = decimal_to_binary(count, bits)

        print(f"{clock}\t{binary}\t{count}")


def frequency_divider():
    print("\n========== FREQUENCY DIVIDER ==========")

    frequency = float(input("Enter input clock frequency (Hz): "))
    division_factor = int(input("Enter division factor: "))

    if frequency <= 0 or division_factor <= 0:
        print("Enter valid positive values.")
        return

    output_frequency = frequency / division_factor

    print(f"\nInput Frequency  = {frequency} Hz")
    print(f"Division Factor  = {division_factor}")
    print(f"Output Frequency = {output_frequency} Hz")


def main():

    while True:

        print("\n==============================================")
        print("        DIGITAL COUNTER CALCULATOR")
        print("        Electrical Engineering")
        print("==============================================")

        print("1. Up Counter")
        print("2. Down Counter")
        print("3. Up/Down Counter")
        print("4. Decade Counter")
        print("5. MOD-N Counter")
        print("6. Frequency Divider")
        print("7. Exit")

        choice = input("\nEnter your choice: ")

        try:

            if choice == "1":
                up_counter()

            elif choice == "2":
                down_counter()

            elif choice == "3":
                up_down_counter()

            elif choice == "4":
                decade_counter()

            elif choice == "5":
                mod_n_counter()

            elif choice == "6":
                frequency_divider()

            elif choice == "7":
                print("\nThank you for using Digital Counter Calculator!")
                break

            else:
                print("\nInvalid choice. Please select 1-7.")

        except ValueError:
            print("\nPlease enter a valid numerical value.")


if __name__ == "__main__":
    main()
