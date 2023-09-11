def belowN(n) -> []:
    result = list()
    if n < 0:
        raise ValueError("error! input value is smaller than 0, it doesn't make sense. Please check your input.")
    elif n == 0:
        print(n)
        return [n]
    elif n > 0:
        if n % 2 == 0:
            print(n)
            result += belowN(n-2)
            result.append(n)
            return result
        else:
            result += belowN(n-1)
            return result

if __name__ == "__main__":
    # print(belowN(10))
    belowN(10)