# Load all relevant libraries
library(dplyr)
library(ggplot2)

# Initialise all variables
w_red = 2
w_blue = 10
n_blue = 24
n_red = 1
w_total = w_red + w_blue*n_blue

# Initialise matrices
blue_term_table <- data.frame(matrix(nrow=n_blue, ncol=1))
colnames(blue_term_table) = 'Value'

red_probability_table <- data.frame(matrix(nrow=n_blue+n_red, ncol=1))
colnames(red_probability_table) = 'Probability_P'

# Calculate the probability of drawing red ball in the first attempt
red_probability_table[1,1] <- w_red/w_total

# Calculate all probabilities
for (k in 2:(n_blue+n_red)) {
  
  # Compute the PI product of all terms
  blue_term <- ((w_total-w_red)-w_blue*(k-2))/(w_total-w_blue*(k-2))
  
  # Compute red ball term
  red_term <- w_red/(w_total-(k-1)*w_blue)
  
  # Record all terms into a result table
  blue_term_table[k-1,1] <- blue_term
  
  # Calculate probability
  red_probability_table[k,1] <- prod(blue_term_table[1:k-1,1])*red_term
  
}



# Compute expected number of draws required to draw the red ball
expected_draws <- sum((1:(n_blue + n_red)) * red_probability_table$Probability_P)
expected_draws

# Compute probabilities P(red in k-th draw)
red_probability_table <- red_probability_table %>%
  mutate(cum_probability = cumsum(Probability_P)) %>%
  rename('Probability P(red in k-th draw)'='Probability_P')

# Plot cumulative probabilities
ggplot(red_probability_table, aes(x = 1:(n_blue + n_red), y = cum_probability)) +
  geom_line() +
  labs(title = "Cumulative Probability of Getting the Floor Treasure with Combined Pity System",
       x = "Draw Number",
       y = "Cumulative Probability") +
  theme_minimal()

