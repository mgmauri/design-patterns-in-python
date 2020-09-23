from __future__ import annotations
import unittest
from abc import ABC, abstractmethod


class Subject(ABC):
    """
    The Subject interface declares a set of methods for managing subscribers.
    """

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """
        Attach an observer to the subject.
        """
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """
        Detach an observer from the subject.
        """
        pass

    @abstractmethod
    def notify(self) -> None:
        """
        Notify all observers about an event.
        """
        pass


class Observer(ABC):
    """
    The Observer interface declares the update method, used by subjects.
    """

    @abstractmethod
    def update(self, subject: Subject) -> None:
        """
        Receive update from subject.
        """
        pass


class Game(Subject):
    """
    The Subject owns some important state and notifies observers when the state
    changes.
    """

    _state: int = None
    """
    For the sake of simplicity, the Subject's state, essential to all
    subscribers, is stored in this variable.
    """

    def __init__(self):
        """

        """
        self._observers: List[Observer] = []

    """
    List of subscribers. In real life, the list of subscribers can be stored
    more comprehensively (categorized by event type, etc.).
    """

    def attach(self, observer: Observer) -> None:
        print("Subject: Attached an observer.")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    """
    The subscription management methods.
    """

    def notify(self) -> None:
        """
        Trigger an update in each subscriber.
        """

        print("Subject: Notifying observers...")
        for observer in self._observers:
            observer.update(self)


class Observer(ABC):
    """
    The Observer interface declares the update method, used by subjects.
    """

    @abstractmethod
    def update(self, subject: Subject) -> None:
        """
        Receive update from subject.
        """
        pass


class Rat(Observer):
    def __init__(self, game):
        """

        """
        self.game = game
        self.game.attach(self)
        self._n_rats = None

    @property
    def attack(self):
        return len(self.game._observers)

    def update(self):
        return self.attack

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.game.detach(self)


class Evaluate(unittest.TestCase):
    def test_single_rat(self):
        game0 = Game()
        rat = Rat(game0)
        self.assertEqual(1, rat.attack)

    def test_two_rats(self):
        game1 = Game()
        rat = Rat(game1)
        rat2 = Rat(game1)
        self.assertEqual(2, rat.attack)
        self.assertEqual(2, rat2.attack)

    def test_three_rats_one_dies(self):
        game = Game()

        rat = Rat(game)
        print(f'rat={rat.attack}')
        self.assertEqual(1, rat.attack)

        rat2 = Rat(game)
        print(f'rat2={rat2.attack}')
        self.assertEqual(2, rat.attack)
        self.assertEqual(2, rat2.attack)
        print(f'rat={rat.attack}')
        with Rat(game) as rat3:
            print(f'rat={rat.attack}')
            self.assertEqual(3, rat.attack)
            self.assertEqual(3, rat2.attack)
            self.assertEqual(3, rat3.attack)

        self.assertEqual(2, rat.attack)
        self.assertEqual(2, rat2.attack)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
