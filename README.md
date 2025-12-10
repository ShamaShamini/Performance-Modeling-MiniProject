# 📘 Performance Modeling and Evaluation of ATM Queue System at Jaffna Market

**Mini Project Report (README Version)**


## 📌 1. System Description & Performance Goal

The ATM Queue System at Jaffna Market, Sri Lanka, consists of **two ATMs ($c=2$)** operated by a single bank, sharing one common queue.

### Key Characteristics

* **Random Arrivals ($\lambda$):** Heavily influenced by market activity (high variability).
* **Variable Service Times ($\mu$):** $1–5$ minutes, depending on the transaction type.
* **ATM Downtimes:** Frequent interruptions due to cash refills or technical failures.
* **Peak Congestion:** Most severe during peak hours (9 AM–12 PM).

### Performance Goal

> 👉 The primary goal is to **minimize customer waiting time ($W_q$)** to effectively reduce congestion and significantly improve user satisfaction.

---

## 📌 2. Modeling Approach & Assumptions

### Modeling Technique

A combined approach was used for comprehensive analysis:

1.  **M/M/2 Analytical Queuing Model:** Used for steady-state performance prediction.
2.  **Discrete-Event Simulation (SimPy):** Used to validate analytical results and model dynamic scenarios like downtime. 

### Key Assumptions (Based on Observation)

| Parameter | Value | Details |
| :--- | :--- | :--- |
| **Arrival rate $\lambda$ (peak)** | 30 customers/hour | $\approx 2$ minutes between arrivals |
| **Arrival rate $\lambda$ (off-peak)** | 15 customers/hour | $\approx 4$ minutes between arrivals |
| **Service rate $\mu$** | 20 customers/hour | Average $\frac{60}{20} = 3$ minutes/customer |
| **Effective $\mu$ (with downtime)** | 18 customers/hour | Reflects $\approx 10\%$ loss in service capacity |
| **Downtime Impact** | 10% | Assumed reduction in server availability |
| **Queue discipline** | FCFS | First-Come, First-Served |
| **No. of ATMs (servers) $c$** | 2 | Primary configuration |

---

## 📌 3. Data Description & Methodology

### Data Collected (1 week study)

* Customer inter-arrival times.
* Service durations for various transactions.
* Observed queue lengths.
* Records of ATM downtime events.

### Observed Values

* **Average service time:** 3 minutes.
* **Peak queue length:** 5–15 customers.
* **Off-peak queue length:** 0–3 customers.

### Methodology: Sensitivity Analysis

The model was subjected to sensitivity analysis to evaluate system resilience:

* **Vary $\lambda$** (arrival rate)
* **Vary $\mu$** (service rate)
* **Vary $c$** (number of ATMs)

The impact was evaluated on the key performance indicators: **Average Waiting Time ($W_q$)** and **Average Queue Length ($L_q$)**.

---

## 🛠️ Requirements

To run this simulation, you will need:

* **Python 3.80** or above

### Libraries

The following Python libraries are required for the simulation and data analysis/visualization:

* `matplotlib`
* `numpy`
* `pandas`
* `sea born`


---

## 📥 Installation

You can clone or download the project files. Once you have the files, install the necessary dependencies using `pip`:

```bash
pip install matplotlib numpy pandas
````

## 🚀 Usage

To run the simulation and view the results, execute the main Python script from your terminal:

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/ShamaShamini/Performance modelling ]
    cd atm_visulaize
    ```
2.  **Run the Simulation:**
    ```bash
    python atm_visulaize.py
    ```

## 📌 4. Analytical Results (M/M/2)

The formulas below were used to derive the steady-state performance metrics (refer to Section 2 for formulas):

### Off-Peak Scenario ($\lambda = 15$ cust/hr)

* **Utilization $\rho$**: $\frac{15}{2 \times 20} = 0.375$
* **Avg Queue Length $L_q$**: $0.18$ customers
* **Avg Waiting Time $W_q$**: $0.72$ min
* **Total Time in System $W$**: $3.72$ min

### Peak Hours Scenario ($\lambda = 30$ cust/hr)

* **Utilization $\rho$**: $\frac{30}{2 \times 20} = 0.75$
* **Avg Queue Length $L_q$**: $2.25$ customers
* **Avg Waiting Time $W_q$**: $4.5$ min
* **Total Time in System $W$**: $7.5$ min

### Downtime Scenario ($\mu = 18$ cust/hr at Peak)

This models the impact of one ATM being temporarily out of service or general service slowdown due to maintenance.

* **Utilization $\rho$**: $\frac{30}{2 \times 18} \approx 0.833$
* **Avg Queue Length $L_q$**: $\approx 4.17$ customers
* **Avg Waiting Time $W_q$**: $\approx 8.34$ min

---

## 📌 5. Simulation Results (SimPy)

The Discrete-Event Simulation (DES) results closely validated the M/M/2 analytical predictions, confirming the model's accuracy.

| Scenario | $W_q$ (Simulated) | $L_q$ (Simulated) | Analytical $W_q$ |
| :--- | :--- | :--- | :--- |
| **Off-peak** | $\approx 0.8$ min | $\approx 0.2$ cust | $0.72$ min |
| **Peak** | $\approx 4.7$ min | $\approx 2.3$ cust | $4.5$ min |
| **Downtime** | $\approx 8.5$ min | $\approx 4.2$ cust | $8.34$ min |

---

## 📌 6. Bottleneck Identification

The analysis highlighted critical factors driving congestion:

* **✔ High Arrival Rate ($\lambda \ge 40$):** Pushes the system close to its stability limit ($\rho \to 1$).
* **✔ ATM Downtime ($\mu = 18$):** The most critical bottleneck; **waiting time almost doubles** (from $4.5$ min to $8.34$ min).
* **✔ Low Service Rate ($\mu$):** Congestion increases sharply if transaction times increase (e.g., system latency).
* **✔ Single ATM Operation ($c=1$):** If one ATM fails, $\rho = \frac{30}{1 \times 20} = 1.5$. Since $\rho > 1$, the queue becomes unstable, growing indefinitely.

---

## 📌 7. Proposed Solutions

Based on the sensitivity analysis, four high-impact solutions are proposed:

| Solution | Strategy | Expected $\boldsymbol{W_q}$ Impact |
| :--- | :--- | :--- |
| **🎯 1. Deploy Mobile ATM ($c=3$)** | **Increase Capacity:** Reduces utilization ($\rho$). | Reduces peak $W_q$ to $\approx 0.6$ minutes. Queue almost disappears. |
| **🎯 2. Transaction Triage System** | **Increase Effective $\mu$:** Prioritize fast transactions (e.g., balance check). | Effective $\mu$ increases, dropping peak $W_q$ to $\approx 2.5$ min. |
| **🎯 3. Predictive Maintenance** | **Maintain Availability:** Schedule downtime only during off-peak hours. | Maintains consistent $c=2$ availability, eliminating the $8.34$ min risk. |
| **🎯 4. Promote Digital Transactions** | **Reduce $\lambda$:** Incentivize digital adoption to shift load. | Reducing $\lambda$ by $20\%$ (to $24$ cust/hr) reduces $W_q$ to $\approx 3$ min. |

---

## 📌 8. Visualizations (Based on Dataset)

The full analysis includes visual evidence supporting the findings:

* **Figure 1: Waiting Time Distribution:** Shows the heavy tail distribution during peak hours.
* **Figure 2: Queue Length Over Time:** Graphs the correlation between arrival rate spikes and queue buildup.
* **Figure 3: Downtime vs Queue Length:** Visually demonstrates the sharp increase in $L_q$ when $c$ effectively drops to 1. 

---

## 📌 9. Limitations

* **Distribution Fit:** Exponential distributions may not perfectly fit real service times (which are often better modeled by deterministic or general distributions).
* **Data Scope:** Analysis is based on limited **one-week data**, potentially missing seasonal variations.
* **Downtime Modeling:** Downtime was modeled simplistically by adjusting $\mu$, rather than a complex breakdown/repair process.
* **Averages:** Steady-state averages hide the real-time fluctuations that cause customer frustration.

## 📌 10. Future Extensions

* **Advanced Modeling:** Employ **M/G/2 or G/G/2 models** for more realistic timing and service time distributions.
* **Real-time Monitoring:** Integrate **IoT-based** monitoring for live performance assessment.
* **Machine Learning:** Develop models for **arrival rate prediction** to dynamically adjust staffing/maintenance.
* **Scalability Evaluation:** Evaluate the long-term optimal capacity for $c=3$ or $c=4$ ATMs.

---

## 📚 References

* Gross & Harris, *Fundamentals of Queueing Theory*
* Jain, *The Art of Computer Systems Performance Analysis*
* SimPy Documentation
* Stewart, *Probability, Markov Chains, Queues, and Simulation*

---

Would you like to explore the implementation details of the SimPy simulation code, or focus on the mathematical derivation of the M/M/2 steady-state probabilities?
