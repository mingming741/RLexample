winning rate matrix:

|                         |   compute_action_function |   RANDOM |   WEAK |   MEDIUM |   STRONG |   RULE_BASED |   ALPHA_PONG |
|:------------------------|--------------------------:|---------:|-------:|---------:|---------:|-------------:|-------------:|
| compute_action_function |                         0 |        1 |      0 |        1 |        1 |            0 |            0 |
| RANDOM                  |                         0 |        1 |      0 |        0 |        0 |            0 |            0 |
| WEAK                    |                         1 |        1 |      1 |        0 |        0 |            1 |            0 |
| MEDIUM                  |                         0 |        1 |      1 |        0 |        0 |            1 |            0 |
| STRONG                  |                         0 |        1 |      1 |        1 |        0 |            1 |            0 |
| RULE_BASED              |                         1 |        1 |      0 |        0 |        0 |            1 |            0 |
| ALPHA_PONG              |                         1 |        1 |      1 |        1 |        1 |            1 |            1 |




reward matrix

|                         |   compute_action_function |   RANDOM |   WEAK |   MEDIUM |   STRONG |   RULE_BASED |   ALPHA_PONG |
|:------------------------|--------------------------:|---------:|-------:|---------:|---------:|-------------:|-------------:|
| compute_action_function |                        -5 |        7 |     -3 |        5 |        7 |           -5 |           -9 |
| RANDOM                  |                        -7 |        1 |    -17 |      -15 |      -13 |          -15 |          -17 |
| WEAK                    |                         3 |       17 |      1 |       -7 |       -3 |           19 |           -5 |
| MEDIUM                  |                        -5 |       15 |      7 |       -3 |       -5 |           11 |           -7 |
| STRONG                  |                        -7 |       13 |      3 |        5 |       -5 |            5 |           -7 |
| RULE_BASED              |                         5 |       15 |    -19 |      -11 |       -5 |            9 |          -17 |
| ALPHA_PONG              |                         9 |       17 |      5 |        7 |        7 |           17 |            3 |