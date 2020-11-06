from pyJoules.energy_meter import measureit
from injected_pyjoules import pyjoules_handler
"""

Original file found here: https://github.com/chad-m/head_tail_breaks_algorithm.git

Python implementation of the head/tail breaks algorithm for classifying heavy-tailed distributions.

Article reference:
http://arxiv.org/ftp/arxiv/papers/1209/1209.2801.pdf

Example:
pareto_data = [(1 / i)**1.16 for i in range(1,100)]  # pareto distribution: x_min=1, a=1.16 (80/20)
htb_pareto = htb(pareto_data)
print(htb_pareto)
[0.03883742394002349, 0.177990388624465, 0.481845351678573]

JavaScript implementation for reference:
function htb(data) {
    var data_mean = data.reduce(function(a, b){return a + b})/data.length;
    var head = data.filter(function(d){return d > data_mean});
    console.log(data_mean);
    while (head.length > 1 && head.length/data.length < 0.40) {
        return htb(head);
    };
}

"""
@measureit(handler=pyjoules_handler.handler)
class HeadTailBreakAlgoV1():

    def htb(self, data):
        """
        Applies the head/tail breaks algorithm to an array of data.

        Params
        ------
        data : list
            Array of data to apply ht-breaks

        Returns
        -------
        results : list
            List of data representing break points
        """
        # test input
        assert data, "Input must not be empty."
        assert all(isinstance(datum, int) or isinstance(datum, float) for datum in data), "All input values must be numeric."

        results = []  # array of break points

        def htb_inner(data):
            """
            Inner ht breaks function for recursively computing the break points.
            """
            if len(data) < 2:
                return []

            # Add mean to results
            data_length = float(len(data))
            data_mean = sum(data) / data_length
            results.append(data_mean)
            head = [datum for datum in data if datum > data_mean]

            # Recursive call to get next break point
            if len(head) / data_length > 0.40:
                return results
            else:
                results.extends(htb_inner(head))
                return results

        htb_inner(data)

        return results

if __name__ == "__main__":
    with open('example/input/input', 'r') as input:
        data = [int(x) for x in input.read().split('\n')]
    HeadTailBreakAlgoV1().htb(data)
