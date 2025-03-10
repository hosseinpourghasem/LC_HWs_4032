import numpy as np
import matplotlib.pyplot as plt

# ضرایب معادله دیفرانسیل
M_alpha = -8.790  # s^-2
M_q = -2.075  # s^-1
M_delta_E = -11.87  # s^-2

# تنظیمات زمان
dt = 0.01  # گام زمانی
T = 5  # کل زمان شبیه‌سازی بر حسب ثانیه
N = int(T / dt)  # تعداد گام‌های زمانی
t = np.linspace(0, T, N)  # بردار زمان

# مقادیر ورودی سکان افقی δ_E بر حسب درجه (تبدیل به رادیان)
delta_E_values = np.radians([-5, 0, 10])  

# تابع حل معادله با روش اویلر
def simulate_pure_pitching(delta_E):
    theta = np.zeros(N)
    theta_dot = np.zeros(N)
    
    for i in range(1, N):
        theta_ddot = M_alpha * theta[i-1] + M_q * theta_dot[i-1] + M_delta_E * delta_E
        theta_dot[i] = theta_dot[i-1] + theta_ddot * dt
        theta[i] = theta[i-1] + theta_dot[i-1] * dt
    
    return theta

# رسم نتایج
plt.figure(figsize=(10, 6))
for delta_E in delta_E_values:
    theta_response = simulate_pure_pitching(delta_E)
    plt.plot(t, theta_response, label=f"δ_E = {np.degrees(delta_E):.0f} deg")

plt.xlabel("Time (s)")
plt.ylabel("Pitch Angle θ (rad)")
plt.title("Pitch Angle Response for Different Elevator Inputs")
plt.legend()
plt.grid()
plt.show()
