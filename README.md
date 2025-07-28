# One Calculator to Calculate Them All

A command‑line Python calculator that computes the volume and cost of “rings” of various sizes, converts units, and tells you how many standard material cubes to buy and the total cost—both for a batch of rings (“Rings of Power”) and for a single ring (“The One Ring”).

---

## 📖 Description

This script (`achu4_211_PA1.py`) guides you through:

1. **Calculating ring volume**  
   - Computes outer volume from user‑entered diameter (cm) and height (mm)
   - Computes inner cutout volume based on a user‑entered ratio
   - Derives net volume of the ring

2. **Unit conversions**  
   - Converts cubic millimeters → cubic inches (1 in³ = 25.4³ mm³)

3. **Material requirements**  
   - Determines how many 1 in³ cubes you must purchase to cover the total net volume

4. **Cost calculations**  
   - For a batch (“Rings of Power”): multiplies number of rings × forging cost and adds material cost
   - For a single ring (“The One Ring”): computes cost similarly on a per‑ring basis

A simple, menu‑style CLI walks you through each prompt and prints formatted results.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.6 or newer

### Installation

```bash
# Clone the repo
git clone https://github.com/your-username/One-Calculator-to-Calculate-Them-All.git
cd One-Calculator-to-Calculate-Them-All
```

## How to Use

python achu4_211_PA1.py

**Follow the prompts:**

One Calculator to Calculate Them All!

Diameter of a ring (in cm)?      
Height of a ring (in mm)?        
Ratio of the inner cutout diameter (as a decimal)?  
Number of rings?                 
Cost of the material (in cents per cubic inch)?  
Forging cost (in cents per ring)?

**Example**

Diameter of a ring (in cm)? 10 <br>
Height of a ring (in mm)? 1 <br>
Ratio of the inner cutout diameter (as a decimal)? 0.5 <br>
Number of rings? 10 <br>
Cost of the material (in cents per cubic inch)? 20 <br>
Forging cost (in cents per ring)? 100 <br>

— Calculations — <br>
Outer volume: X mm³ <br>
Inner cutout volume: Y mm³ <br>
Net volume: Z mm³ <br>
Material needed: N cubes (1 in³ each) <br>
Total cost for 10 rings: $A.BC <br>
Cost per ring: $D.EF <br>

## Run Test Cases

python tester1.py achu4_211_PA1.py


