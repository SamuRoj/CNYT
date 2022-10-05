import unittest
import LibQuantum
import Matrix_Lib as Ml


class MyTestCase(unittest.TestCase):
    def test_something(self):
        print("Juego de las canicas con matrices booleanas.")
        Ml.print_vector(LibQuantum.MarblesGame(LibQuantum.m1, LibQuantum.v1, 5))
        self.assertAlmostEqual(LibQuantum.MarblesGame(LibQuantum.m1, LibQuantum.v1, 5), ((0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (27, 0)))
        print()
        print("Juego de las canicas con las entradas de las matrices como fracciones.")
        Ml.print_vector(LibQuantum.DecimalSlits(LibQuantum.m2, LibQuantum.v2, 1))
        self.assertAlmostEqual(LibQuantum.DecimalSlits(LibQuantum.m2, LibQuantum.v2, 1), ((0.416665, 0.0), (0.25, 0.0), (0.333335, 0.0)))
        print()
        print("Experimento múltiples rendijas clásico probabilístico.")
        Ml.print_vector(LibQuantum.MultipleSlits(LibQuantum.m3, LibQuantum.v3, 2, 5, 2))
        self.assertAlmostEqual(LibQuantum.MultipleSlits(LibQuantum.m3, LibQuantum.v3, 2, 5, 2), ((0.0, 0.0), (0.0, 0.0), (0.0, 0.0), (0.16667, 0.0), (0.16667, 0.0), (0.33333, 0.0), (0.16667, 0.0), (0.16667, 0.0)))
        print()
        print("Experimento múltiples rendijas cuántico.")
        Ml.print_vector(LibQuantum.MultipleSlitsQuantum(LibQuantum.m4, LibQuantum.v3, 2, 5, 2))
        self.assertAlmostEqual(LibQuantum.MultipleSlitsQuantum(LibQuantum.m4, LibQuantum.v3, 2, 5, 4), ((0.0, 0.0), (0.0, 0.0), (0.0, 0.0), (0.16667, 0.0), (0.16667, 0.0), (0.0, 0.0), (0.16667, 0.0), (0.16667, 0.0)))
        print()
        print("Verificación del fenómeno de interferencia.")
        print(LibQuantum.Interference(LibQuantum.MultipleSlits(LibQuantum.m3, LibQuantum.v3, 2, 5, 2), LibQuantum.MultipleSlitsQuantum(LibQuantum.m4, LibQuantum.v3, 2, 5, 2)))
        self.assertAlmostEqual(LibQuantum.Interference(LibQuantum.MultipleSlits(LibQuantum.m3, LibQuantum.v3, 2, 5, 2), LibQuantum.MultipleSlitsQuantum(LibQuantum.m4, LibQuantum.v3, 2, 5, 2)), "Hay interferencia.")
        LibQuantum.BarGraph(LibQuantum.MultipleSlits(LibQuantum.m3, LibQuantum.v3, 2, 5, 2))

if __name__ == '__main__':
    unittest.main()
