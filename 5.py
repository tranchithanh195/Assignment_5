import random
def estimate_pi():
    total_points = int(input("How many random points should be generated? "))
    points_inside_circle = 0

    for _ in range(total_points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if x ** 2 + y ** 2 < 1:
            points_inside_circle += 1
    pi_approximation = 4 * points_inside_circle / total_points
    print(f"The approximate value of pi is: {pi_approximation}")

if __name__ == "__main__":
    estimate_pi()
