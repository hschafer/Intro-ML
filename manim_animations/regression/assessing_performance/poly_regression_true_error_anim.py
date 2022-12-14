from sklearn.metrics import mean_squared_error

from ap_utils import *
from poly_regression_with_error_scene import (DATA_X_RANGE,
                                              PolyRegressionWithErrorScene)

TRUE_ERROR_Y_RANGE = (0, 8)
TEST_RANGE_BUFFER = 2

def error_fn(p):
    # All magic numbers to make the graph look nice
    # https://mycurvefit.com/
    result = 2.134554 - 0.02247024 * p - 0.1709821 * p ** 2 + 0.02604167 * p ** 3
    result = result + 0.6 / (1 + 2 * p) + 0.5
    return result


class Animation(PolyRegressionWithErrorScene):
    def __init__(self, **kwargs):
        super().__init__("Training Data", "True Error", error_fn,
                error_y_range=TRUE_ERROR_Y_RANGE, **kwargs)

    def loss_fn(self, deg):
        # Test all points between a range. Focus in middle of range to get more intuitive results
        n_test = 1000
        X_test = np.linspace(DATA_X_RANGE[0] + TEST_RANGE_BUFFER, DATA_X_RANGE[1] - TEST_RANGE_BUFFER, n_test).reshape((n_test, 1))
        X_test, y_test = generate_train_data(Xs=X_test)


        model = train(self.Xs, self.ys, deg)
        y_test_hat = model.predict(X_test)
        return mean_squared_error(y_test, y_test_hat)
