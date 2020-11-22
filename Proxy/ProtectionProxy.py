class Car:
    def __init__(self, driver):
        self.driver = driver

    def drive(self):
        print(f"Car is being  driven by {self.driver.name}")


class CarProxy:

    def __init__(self,driver):
        self.driver = driver
        self._car = Car(driver)

    def drive(self):
        age_limit = 18
        if self.driver.age >= age_limit:
            self._car.drive()
        else:
            return print(f"{self.driver.name} is too young to drive. \nTo Drive a car,{self.driver.name} have to wait for "
                         f"{age_limit -self.driver.age } years.")


class Driver:
    def __init__(self, name, age):
        self.name = name
        self.age = age



if __name__ == '__main__':
    driver = Driver("John",10)
    car = CarProxy(driver)
    car.drive()
