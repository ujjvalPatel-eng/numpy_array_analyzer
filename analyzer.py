import numpy as np


class DataAnalytics:
    def __init__(self):
        self.__arr = None

    def create_array(self):
        while True:
            print("=" * 15)
            print("\n1. create 1D array".title())
            print("2. create 2D array".title())
            print("3. create 3D array".title())

            dimension = str(input("chose a dimension (1-3): "))
            match dimension:
                case "1":
                    try:
                        self.__arr = np.array(
                            input(f"Enter elements for array (seprated by space): ")
                            .strip()
                            .split(),
                            dtype=int,
                        )
                    except ValueError:
                        print("Invalid input! Please enter integers.")
                    else:
                        self.__arr = self.__arr.astype(int)
                        print(f"\n1D array: {self.__arr}")
                        break
                case "2":
                    try:
                        row = int(input("\nEnter number of rows: "))
                        col = int(input("Enter number of columns: "))

                        self.__arr = np.array(
                            input(
                                f"Enter {row*col} elements for array (seprated by space): "
                            )
                            .strip()
                            .split(),
                            dtype=int,
                        )
                        self.__arr = self.__arr.astype(int)
                        self.__arr = self.__arr.reshape(row, col, copy=False)
                        print(f"\n 2D Array: \n{self.__arr}")
                    except ValueError:
                        print("Invalid input! Please enter integers.")
                    break
                case "3":
                    row = int(input("\nEnter number of rows: "))
                    col = int(input("Enter number of columns: "))
                    layer = int(input("Enter Number of layers:"))

                    try:
                        self.__arr = np.array(
                            input(
                                f"Enter {row*col*layer} elements for array (seprated by space): "
                            )
                            .strip()
                            .split(),
                            dtype=int,
                        )
                        self.__arr = self.__arr.astype(int)
                        self.__arr = self.__arr.reshape(row, col, layer, copy=False)
                        print(f"\n 3D Array: \n{self.__arr}")
                    except ValueError:
                        print("Invalid input! Please enter integers.")
                    break
                case _:
                    print("choose a valid option (1-3)")

    def Indexing_and_slicing(self):
        while True:
            print("=" * 15)
            print("\n1. Indexing")
            print("2. Slicing")
            print("3. Back to main menu")

            option = input("choose your option (1-3): ".title())

            match option:
                case "1":
                    if self.__arr is None:
                        print("No array found!")
                        return

                    dim = self.__arr.ndim

                    print("\nCurrent Array:")
                    print(self.__arr)

                    # ==========================
                    # 1D ARRAY
                    # ==========================
                    if dim == 1:
                        try:
                            index = int(input("\nEnter index: "))

                            print("Result:", self.__arr[index])
                        except IndexError:
                            print("Index out of bounds! Please enter valid indices.")

                    # ==========================
                    # 2D ARRAY
                    # ==========================
                    elif dim == 2:

                        try:
                            row = int(input("\nEnter row index: "))
                            col = int(input("Enter column index: "))

                            print("Result:", self.__arr[row, col])
                        except IndexError:
                            print("Index out of bounds! Please enter valid indices.")

                    # ==========================
                    # 3D ARRAY
                    # ==========================
                    elif dim == 3:

                        try:
                            layer = int(input("\nEnter layer index: "))
                            row = int(input("Enter row index: "))
                            col = int(input("Enter column index: "))

                            print("Result:", self.__arr[layer, row, col])
                        except IndexError:
                            print("Index out of bounds! Please enter valid indices.")

                    else:
                        print("Indexing for dimensions > 3 not supported")

                case "2":
                    if self.__arr is None:
                        print("No array found!")
                        return

                    dim = self.__arr.ndim

                    print("\nCurrent Array:")
                    print(self.__arr)

                    if dim == 1:

                        start = int(input("\nEnter start index: "))
                        end = int(input("Enter end index: "))

                        print("Result:")
                        print(self._DataAnalytics__arr[start:end])

                    elif dim == 2:

                        row_start = int(input("\nRow start: "))
                        row_end = int(input("Row end: "))

                        col_start = int(input("Column start: "))
                        col_end = int(input("Column end: "))

                        print("Result:")
                        print(
                            self._DataAnalytics__arr[
                                row_start:row_end, col_start:col_end
                            ]
                        )

                    elif dim == 3:

                        layer_start = int(input("\nLayer start: "))
                        layer_end = int(input("Layer end: "))

                        row_start = int(input("Row start: "))
                        row_end = int(input("Row end: "))

                        col_start = int(input("Column start: "))
                        col_end = int(input("Column end: "))

                        print("Result:")
                        print(
                            self._DataAnalytics__arr[
                                layer_start:layer_end,
                                row_start:row_end,
                                col_start:col_end,
                            ]
                        )

                    else:
                        print("Slicing for dimensions > 3 not supported")

    def combine(self):
        if self.__arr is None:
            print("No array found!")
            return

        dim = self.__arr.ndim
        arr2 = None

        print("\nCurrent Array:")
        print(self.__arr)

        print("\nEnter another array with SAME dimensions")

        if dim == 1:

            elements = input("\nEnter elements separated by space: ").split()

            arr2 = np.array(elements, dtype=int)

        elif dim == 2:

            rows = int(input("\nEnter rows: "))
            cols = int(input("Enter columns: "))

            total = rows * cols

            elements = input(f"Enter {total} elements separated by space: ").split()

            arr2 = np.array(elements, dtype=int).reshape(rows, cols)

        elif dim == 3:

            layers = int(input("\nEnter layers: "))
            rows = int(input("Enter rows: "))
            cols = int(input("Enter columns: "))

            total = layers * rows * cols

            elements = input(f"Enter {total} elements separated by space: ").split()

            arr2 = np.array(elements, dtype=int).reshape(layers, rows, cols)

        print("\n1. Horizontal Combine")
        print("2. Vertical Combine")

        match choice:

            case "1":
                result = np.hstack((self.__arr, arr2))

            case "2":
                result = np.vstack((self.__arr, arr2))

            case _:
                print("Invalid Choice")
                return

    def split(self):
        if self.__arr is None:
            print("No array found!")
            return

        dim = self.__arr.ndim

        print("\nCurrent Array:")
        print(self.__arr)

        if dim == 1:

            num_splits = int(input("\nEnter number of splits: "))

            result = np.array_split(self.__arr, num_splits)

        elif dim == 2:

            print("\n1. Split by rows")
            print("2. Split by columns")

            choice = input("Choose an option (1-2): ")

            if choice == "1":
                num_splits = int(input("\nEnter number of splits: "))
                result = np.array_split(self.__arr, num_splits, axis=0)

            elif choice == "2":
                num_splits = int(input("\nEnter number of splits: "))
                result = np.array_split(self.__arr, num_splits, axis=1)

            else:
                print("Invalid Choice")
                return

        elif dim == 3:

            print("\n1. Split by layers")
            print("2. Split by rows")
            print("3. Split by columns")

            choice = input("Choose an option (1-3): ")

            if choice == "1":
                num_splits = int(input("\nEnter number of splits: "))
                result = np.array_split(self.__arr, num_splits, axis=0)

            elif choice == "2":
                num_splits = int(input("\nEnter number of splits: "))
                result = np.array_split(self.__arr, num_splits, axis=1)

            elif choice == "3":
                num_splits = int(input("\nEnter number of splits: "))
                result = np.array_split(self.__arr, num_splits, axis=2)

            else:
                print("Invalid Choice")
                return

        else:
            print("Splitting for dimensions > 3 not supported")
            return


# ==================================
# SORT ARRAY
# ==================================
def sort_array(self):

    if self.__arr is None:
        print("No array found!")
        return

    print("\nCurrent Array:")
    print(self.__arr)

    dim = self.__arr.ndim

    # ==================================
    # 1D ARRAY
    # ==================================
    if dim == 1:

        result = np.sort(self.__arr)

    # ==================================
    # 2D ARRAY
    # ==================================
    elif dim == 2:

        print("\n1. Sort Row Wise")
        print("2. Sort Column Wise")

        choice = input("Choose option: ")

        match choice:

            case "1":
                result = np.sort(self.__arr, axis=1)

            case "2":
                result = np.sort(self.__arr, axis=0)

            case _:
                print("Invalid Choice")
                return

    # ==================================
    # 3D ARRAY
    # ==================================
    elif dim == 3:

        print("\n1. Sort Along Layers")
        print("2. Sort Along Rows")
        print("3. Sort Along Columns")

        choice = input("Choose option: ")

        match choice:

            case "1":
                result = np.sort(self.__arr, axis=0)

            case "2":
                result = np.sort(self.__arr, axis=1)

            case "3":
                result = np.sort(self.__arr, axis=2)

            case _:
                print("Invalid Choice")
                return

    else:
        print("Dimensions greater than 3 not supported")
        return

    print("\nSorted Array:")
    print(result)


# ==================================
# SEARCH ELEMENT
# ==================================
def search_array(self):

    if self.__arr is None:
        print("No array found!")
        return

    print("\nCurrent Array:")
    print(self.__arr)

    value = int(input("\nEnter element to search: "))

    result = np.where(self.__arr == value)

    # ELEMENT FOUND
    if len(result[0]) > 0:

        print("\nElement Found!")

        dim = self.__arr.ndim

        # ==================================
        # 1D ARRAY
        # ==================================
        if dim == 1:

            for i in result[0]:

                print(f"Index: {i}")

        # ==================================
        # 2D ARRAY
        # ==================================
        elif dim == 2:

            for row, col in zip(result[0], result[1]):

                print(f"Row: {row}, Column: {col}")

        # ==================================
        # 3D ARRAY
        # ==================================
        elif dim == 3:

            for layer, row, col in zip(result[0], result[1], result[2]):

                print(f"Layer: {layer}, " f"Row: {row}, " f"Column: {col}")

    else:
        print("Element not found!")


# ==================================
# FILTER ARRAY
# ==================================
def filter_array(self):

    if self.__arr is None:
        print("No array found!")
        return

    print("\nCurrent Array:")
    print(self.__arr)

    print("\n1. Greater Than")
    print("2. Less Than")
    print("3. Equal To")

    choice = input("\nChoose condition: ")

    value = int(input("Enter value: "))

    match choice:

        # GREATER THAN
        case "1":

            result = self.__arr[self.__arr > value]

            print(f"\nElements Greater Than {value}:")
            print(result)

        # LESS THAN
        case "2":

            result = self.__arr[self.__arr < value]

            print(f"\nElements Less Than {value}:")
            print(result)

        # EQUAL TO
        case "3":

            result = self.__arr[self.__arr == value]

            print(f"\nElements Equal To {value}:")
            print(result)

        case _:
            print("Invalid Choice")


def mathamatical_functions(self):

    if self.__arr is None:
        print("No array found!")
        return

    dim = self.__arr.ndim

    print("\nCurrent Array:")
    print(self.__arr)

    print("\n1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("\nChoose operation (1-4): ")

    # ==================================
    # 1D ARRAY
    # ==================================
    if dim == 1:

        elements = input("\nEnter elements separated by space: ").split()

        arr2 = np.array(elements, dtype=int)

    # ==================================
    # 2D ARRAY
    # ==================================
    elif dim == 2:

        rows = int(input("\nEnter rows: "))
        cols = int(input("Enter columns: "))

        total = rows * cols

        elements = input(f"Enter {total} elements separated by space: ").split()

        arr2 = np.array(elements, dtype=int).reshape(rows, cols)

    # ==================================
    # 3D ARRAY
    # ==================================
    elif dim == 3:

        layers = int(input("\nEnter layers: "))
        rows = int(input("Enter rows: "))
        cols = int(input("Enter columns: "))

        total = layers * rows * cols

        elements = input(f"Enter {total} elements separated by space: ").split()

        arr2 = np.array(elements, dtype=int).reshape(layers, rows, cols)

    else:
        print("Dimensions greater than 3 not supported")
        return

    # ==================================
    # OPERATIONS
    # ==================================
    match choice:

        # ADDITION
        case "1":

            result = self.__arr + arr2

            print("\nAddition Result:")
            print(result)

        # SUBTRACTION
        case "2":

            result = self.__arr - arr2

            print("\nSubtraction Result:")
            print(result)

        # MULTIPLICATION
        case "3":

            result = self.__arr * arr2

            print("\nMultiplication Result:")
            print(result)

        # DIVISION
        case "4":

            if np.any(arr2 == 0):

                print("Division by zero is not allowed!")
                return

            result = self.__arr / arr2

            print("\nDivision Result:")
            print(result)

        case _:
            print("Invalid Choice")
    # ==================================


# ARRAY STATISTICS
# ==================================
def array_statistics(self):

    if self.__arr is None:
        print("No array found!")
        return

    print("\nCurrent Array:")
    print(self.__arr)

    print("\n1. Mean")
    print("2. Median")
    print("3. Standard Deviation")
    print("4. Variance")

    choice = input("\nChoose option (1-4): ")

    match choice:

        case "1":

            result = np.mean(self.__arr)
            print("\nMean:")
            print(result)

        case "2":

            result = np.median(self.__arr)
            print("\nMedian:")
            print(result)

        case "3":

            result = np.std(self.__arr)
            print("\nStandard Deviation:")
            print(result)

        case "4":

            result = np.var(self.__arr)
            print("\nVariance:")
            print(result)

        case _:
            print("Invalid Choice")


obj = DataAnalytics()
print("--" * 15)
print("Welcome to Numpy analyzer".title())
print("--" * 15)

while True:
    print("\n1. Create a numpy array".title())
    print("2. Indexing and slicing".title())
    print("3. perform mathamatical function".title())
    print("4. combine or split array".title())
    print("5. search, sort or filter arrays".title())
    print("6. compute aggrigate and statistics".title())
    print("7. Exit")

    choice = str(input("Choose an option (1-7):"))

    match choice:
        case "1":
            obj.create_array()

        case "2":
            obj.Indexing_and_slicing()
        case "3":
            obj.mathamatical_functions()
        case "4":
            while True:
                print("\n1. Combine arrays")
                print("2. Split array")
                print("3. Back to main menu")

                sub_choice = input("Choose an option (1-3): ")

                if sub_choice == "1":
                    obj.combine()
                elif sub_choice == "2":
                    obj.split()
                elif sub_choice == "3":
                    break
                else:
                    print("Invalid choice! Please choose a valid option.")
        case "5":
            while True:
                print("\n1. Search element")
                print("2. Sort array")
                print("3. Filter array")
                print("4. Back to main menu")

                sub_choice = input("Choose an option (1-4): ")
                match sub_choice:
                    case "1":
                        obj.search_array()
                    case "2":
                        obj.sort_array()
                    case "3":
                        obj.filter_array()
                    case "4":
                        break
                    case _:
                        print("Invalid choice! Please choose a valid option.")
        case "6":
            obj.array_statistics()
        case "7":
            print("Exiting... Goodbye!")
            break
        case _:
            print("Invalid choice! Please choose a valid option. (1-7)")
