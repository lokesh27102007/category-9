
p_disease = 0.01
p_positive_given_disease = 0.90
p_positive_given_no_disease = 0.05

p_no_disease = 1 - p_disease

p_positive = (
    p_positive_given_disease * p_disease +
    p_positive_given_no_disease * p_no_disease
)

posterior = (
    p_positive_given_disease * p_disease
) / p_positive

print("Probability of disease after positive test:",
      round(posterior, 4))
