from namespaced.a import func_a
from namespaced.b import func_b

from c import func_c


def main():
    print(func_a())
    print(func_b())
    print(func_c())

if __name__ == "__main__":
    main()
