{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "xEt6HbN0b7q8"
   },
   "source": [
    "# **Workshop : Introduction to Julia**   ..............................                                             <img src=\"https://github.com/JuliaLang/julia-logo-graphics/raw/master/images/julia-logo-color.png\" height=\"60\" /> ............................\n",
    "\n",
    "\n",
    "# *Objectives*\n",
    "* Introduction to Julia \n",
    "  * Basics of Julia :  a brief backgound.\n",
    "  * Setting up Julia IDE or REPL Environment.\n",
    "* Hands on with Julia\n",
    "   * Variables and Data Types.\n",
    "   * Functions.\n",
    "   * Data Structures.\n",
    "   * Control Flow.\n",
    "\n",
    "# *Future Topics*\n",
    "\n",
    "Varibale Scope, Modules, Packages, Plotting, Parallel computing, Code Optimization and Interoperability.\n",
    "   \n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "mopW6FKfHG7h"
   },
   "source": [
    "\n",
    "# **Introduction to Julia**  \n",
    "  Julia has evolved quickly since its inception in 2012.\n",
    "  * Julia user base has grown significantly with high profile users like NASA,  BlackRock, Aviva and INPE.\n",
    "  * Julia is the only programming language to win _James H. Wilkinson Prize for Numerical Software_. \n",
    "  * Julia is general purpose programming language with wide range of applications, including _data science, complex linear algebra, data mining, and machine learning_. \n",
    "\n",
    "\n",
    "# **Julia _vs._ C++/C _vs._ Python**\n",
    "\n",
    " Julia feels like python but runs like C++/C. Infact julia gives you an option to write your code with much flexibility. You can code like python or to boost profermance you type everything statistically like C++.\n",
    " \n",
    "# **Ways to run Julia**\n",
    "\n",
    "Three ways to run Julia code: \n",
    "  * the first one is through the Julia REPL,\n",
    "  * through the IDE: _Juno , VSCode_, and\n",
    "  * Cloud Platforms: _Colab, Kaggle, CoCalc, Azure etc_.\n",
    "\n",
    "# **Google Colabs Instructions**\n",
    "\n",
    "* Execute the following cell (click on it and press Ctrl+Enter) to install Julia, IJulia and other packages (if needed, update JULIA_VERSION and the other parameters). This takes a couple of minutes.\n",
    "*Reload this page (press Ctrl+R, or ⌘+R, or the F5 key) and continue to the next section.\n",
    "\n",
    "*Notes:*\n",
    "\n",
    "* If your Colab Runtime gets reset (e.g., due to inactivity), repeat steps 2, 3 and 4.\n",
    "* After installation, if you want to change the Julia version or activate/deactivate the GPU, you will need to reset the Runtime: Runtime > Factory reset runtime and repeat steps 3 and 4.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "id": "OMnAG0sYt8IP"
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "UsageError: Cell magic `%%shell` not found.\n"
     ]
    }
   ],
   "source": [
    "%%shell\n",
    "set -e\n",
    "\n",
    "#---------------------------------------------------#\n",
    "JULIA_VERSION=\"1.7.1\" # any version ≥ 0.7.0\n",
    "JULIA_PACKAGES=\"IJulia BenchmarkTools Plots\"\n",
    "JULIA_PACKAGES_IF_GPU=\"CUDA\" # or CuArrays for older Julia versions\n",
    "JULIA_NUM_THREADS=2\n",
    "#---------------------------------------------------#\n",
    "\n",
    "if [ -n \"$COLAB_GPU\" ] && [ -z `which julia` ]; then\n",
    "  # Install Julia\n",
    "  JULIA_VER=`cut -d '.' -f -2 <<< \"$JULIA_VERSION\"`\n",
    "  echo \"Installing Julia $JULIA_VERSION on the current Colab Runtime...\"\n",
    "  BASE_URL=\"https://julialang-s3.julialang.org/bin/linux/x64\"\n",
    "  URL=\"$BASE_URL/$JULIA_VER/julia-$JULIA_VERSION-linux-x86_64.tar.gz\"\n",
    "  wget -nv $URL -O /tmp/julia.tar.gz # -nv means \"not verbose\"\n",
    "  tar -x -f /tmp/julia.tar.gz -C /usr/local --strip-components 1\n",
    "  rm /tmp/julia.tar.gz\n",
    "\n",
    "  # Install Packages\n",
    "  if [ \"$COLAB_GPU\" = \"1\" ]; then\n",
    "      JULIA_PACKAGES=\"$JULIA_PACKAGES $JULIA_PACKAGES_IF_GPU\"\n",
    "  fi\n",
    "  for PKG in `echo $JULIA_PACKAGES`; do\n",
    "    echo \"Installing Julia package $PKG...\"\n",
    "    julia -e 'using Pkg; pkg\"add '$PKG'; precompile;\"' &> /dev/null\n",
    "  done\n",
    "\n",
    "  # Install kernel and rename it to \"julia\"\n",
    "  echo \"Installing IJulia kernel...\"\n",
    "  julia -e 'using IJulia; IJulia.installkernel(\"julia\", env=Dict(\n",
    "      \"JULIA_NUM_THREADS\"=>\"'\"$JULIA_NUM_THREADS\"'\"))'\n",
    "  KERNEL_DIR=`julia -e \"using IJulia; print(IJulia.kerneldir())\"`\n",
    "  KERNEL_NAME=`ls -d \"$KERNEL_DIR\"/julia*`\n",
    "  mv -f $KERNEL_NAME \"$KERNEL_DIR\"/julia  \n",
    "\n",
    "  echo ''\n",
    "  echo \"Successfully installed `julia -v`!\"\n",
    "  echo \"Please reload this page (press Ctrl+R, ⌘+R, or the F5 key) then\"\n",
    "  echo \"jump to the 'Checking the Installation' section.\"\n",
    "fi"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# REPL allows you to execute code line by line\n",
    "\n",
    "**Basic arithmetic operations**\n",
    "* _Number Addition_\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 218,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "7"
      ]
     },
     "execution_count": 218,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "3+4"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "* subtraction, addition, multiplication, power, square-root, log etc."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 217,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "-2\n",
      "92\n",
      "16\n",
      "9.591663046625438\n",
      "5.830951894845301\n",
      "3.1354942159291497\n"
     ]
    }
   ],
   "source": [
    "println(4-6)\n",
    "println(4*23)\n",
    "println(4^2)\n",
    "println(√92)\n",
    "println(sqrt(34))\n",
    "println(log(23))\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Boolean/Logical operators** \n",
    "*  _&, xor, ||, nand_"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "true\n",
      "false\n",
      "true\n",
      "true\n"
     ]
    }
   ],
   "source": [
    "println(true || false)\n",
    "println(true & false)\n",
    "println(xor(true, false))\n",
    "println(nand(true,false))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Precision\n",
    "* _Float + Int Addition_\n",
    "<div>\n",
    "    <img src=\"enlightenment-symbol.png\"  width=\"50\"  />\n",
    " </div>    \n",
    "\n",
    "* _Resultant data type is same as highest precision operand_\n",
    " "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "7.0"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "2 + 5.0"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Basic Complex Numbers operations**\n",
    "* _Complex Number Addition_"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3 + 4im"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "3+4im"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "-42 + 25im"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "(3+2im)-(45-23im)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Basic Fractional Numbers operations**\n",
    "* _Fraction Representioan_"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3//5"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "3//5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "51//10"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "3//5 + 9//2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "223//21"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "34//21 + 9"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**How to know the type of variable**\n",
    "<div>\n",
    "   <img src=\"enlightenment-symbol.png\"  width=\"50\"  />\n",
    " </div>  \n",
    " \n",
    " _typeof(variable)_ \n",
    "\n",
    "**will let you know the type inferred by Julia**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Int64"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "typeof(1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Rational{Int64}"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "typeof(34//20 + 9)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Complex{Int64}"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "typeof(4+7im)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "S8PHGPQ8vVXm"
   },
   "source": [
    "# **Variables and Types**"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "* Julia let you declare a vaiable without explietly mantion the datatype.\n",
    "* Julia infered its type based on the value assigned to it.\n",
    "<div>\n",
    "     <img src=\"enlightenment-symbol.png\"  width=\"50\"  />  \n",
    "</div>\n",
    "<div>\n",
    "   <img src=\"Datatypes.png\"  width=\"500\"  /> <img src=\"enlightenment-symbol.png\"  width=\"50\"  />  \n",
    " </div>  \n",
    "\n",
    "**From performance point of view, you should not change the datatype after its intialization**"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Declaring and Initializing Variables\n",
    "* **value is a vaiable name as is assigned a vaue using = operator**\n",
    "* **Variables in Julia can be declared by just writing their name. There’s no need to define a datatype with it.**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {
    "id": "klAmDZrxyIMs"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "value = 5"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Rules for naming a variable in Julia\n",
    "* Variable names in Julia must start with an underscore, a letter(A-Z or a-z) or a Unicode character greater than 00A0(nbsp).\n",
    "* Variable names can also contain digits(0-9) or !, but must not begin with these.\n",
    "* Operators like (+, ^, etc.) can also be used to name a variable.\n",
    "* Variable names can also be written as words seperated by underscore, but that is not a good practice and must be avoided unless necessary.\n",
    "* LaTeX sybols as variable names; Help in succict and readable mathematic functions"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {
    "id": "Rrwzz2uOAPXZ"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "23"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "θ = 5\n",
    "Θ = 9\n",
    "ϕ = 9\n",
    "Φ = 23\n",
    "ϵ = 9\n",
    "ζ = 23\n",
    "κ = 23\n",
    "δ = 23\n",
    "Δ  = 23\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Statically Typed *Variable* Names"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 171
    },
    "id": "gNWIQmb7ARce",
    "outputId": "37ed7026-da94-4b72-d15f-72f41a4cefb0"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x = 5::Int64"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "-9223372036854775808\n",
      "9223372036854775807"
     ]
    }
   ],
   "source": [
    "print(typemin(Int64),\"\\n\")\n",
    "print(typemax(Int64))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "String"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x = \"345\"::String\n",
    "typeof(x)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "tags": []
   },
   "source": [
    "## Type Conversion\n",
    "* Use _convert function (targettype,varibale)_\n",
    "* Always from low to high precision.\n",
    "* Use trunc/floor etc. to get to lower precision."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3.0\n"
     ]
    }
   ],
   "source": [
    "x = 3\n",
    "println(convert(Float64,x))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## String to Number Conversion in Julia\n",
    "* Parse function (T::Type, str, base=Int)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10004\n",
      "23424\n",
      "144420\n"
     ]
    }
   ],
   "source": [
    "println(parse(Int64,\"23424\",base = 8))\n",
    "println(parse(Int64,\"23424\",base = 10))\n",
    "println(parse(Int64,\"23424\",base = 16))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# **String Initialization and Operators**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "University of Cincinnati\n",
      "sf\n",
      "abcdefgef\n"
     ]
    }
   ],
   "source": [
    "x = \"University of Cincinnati\"\n",
    "println(x)\n",
    "println(string(\"sf\"))\n",
    "println(string(\"abc\",\"def\",\"gef\"))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## String Indexing, Slicing and Operators\n",
    "\n",
    "* x[1]- first character, x[2] = second character. **Indexing**\n",
    "* x[2:4]- second to fourth character **Slicing**\n",
    "* x[-1]- backward slicing \n",
    "* _*_ Concatination Operation\n",
    "* ^ repetition\n",
    "* Use _begin_ and _end_ to access string from front and back respectively"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "UC\n",
      "is\n",
      "University of Cincinnati\n",
      "at\n",
      "Cincinnati\n"
     ]
    }
   ],
   "source": [
    "println(x[1],x[15])\n",
    "println(x[3],x[7])\n",
    "println(x[begin:end])\n",
    "println(x[end-2:end-1])\n",
    "println(x[end-9:end])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "QriGo9JvCHcg"
   },
   "source": [
    "# **Comments** \n",
    "* Single Line Comment"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [],
   "source": [
    "#This is Single Line Comment"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "* Multiple Line Comments"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {
    "id": "JpZ5HpQyAiXm"
   },
   "outputs": [],
   "source": [
    "#= This\n",
    "is\n",
    "mulitple Line\n",
    "Comment\n",
    "=#"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "YfTcYznkApt5"
   },
   "source": [
    "# Hands-on  **Variable and Datatype**\n",
    "<div>\n",
    "     <img src=\"Handson.png\"  width=\"100\"  />  \n",
    "</div>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "LH9k7gmRAoqg"
   },
   "source": [
    "### The Rule of 72 applies to cases of compound interest. \n",
    "**Compound interest is calculated on both the initial principal and the accumulated interest of previous periods of a deposit.**\n",
    "* To calculate the time period an investment will double, divide the integer 72 by the expected rate of return. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "12.0"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# You have 10,000 in you bank account\n",
    "\n",
    "#= Bank Provides you an annual interest rate of 6% =#\n",
    "time = 72/6\n",
    "# Find the time in which your fortune doubles.\n",
    "#12 - 20,000\n",
    "# When Will you become millionaire\n",
    "\n",
    "#24 - 40,000\n",
    "#36 - 80,000\n",
    "#48 - 1,60,000\n",
    "#60 - 3,20,000\n",
    "#72 - 6,40,000\n",
    "#84 - 12,80,000\n",
    "#96 - 25,60,000\n",
    "#108 - 51,20,000\n",
    "#120 - 1,0240,000\n",
    "\n",
    "# When Will you become billionaire\n",
    "\n",
    "#2^time *10000 = 12*time\n",
    "#(72/interest)*t = 2^t*principle\n",
    "\n",
    "#2^t = 1,000,000,000/10,000 = 100,000\n",
    "#t = log(100,000)\n",
    "#time = 100\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "159.45254855459342"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "log(2,100000000/10000)*12"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "reuiMdtcvrBm"
   },
   "source": [
    "# **Functions**\n",
    "* #### Operators are _functions_ and written in **infix** notation\n",
    "  * Boolean/Logical. \n",
    "  ### (&,   ||,    xor,   nand)\n",
    "  * Arithmatic. \n",
    "  ### ( +,  -,  /,  *,  √,  ^,  log etc.)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "7\n",
      "0.75\n",
      "12\n",
      "81\n"
     ]
    }
   ],
   "source": [
    "println(+(3,4))\n",
    "println(/(3,4))\n",
    "println(*(3,4))\n",
    "println(^(3,4))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "\n",
    "## Generic Functions\n",
    "  \n",
    "### **Standard Definition.**\n",
    "  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {
    "id": "W4rvs_tYvqRh"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "squareroot (generic function with 1 method)"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "function squareroot(a)\n",
    "    return √a\n",
    "end"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "squareroot (generic function with 1 method)"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "function squareroot(a) ::Float64\n",
    "    return √a\n",
    "end"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " ### **Inline Functions.**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "f (generic function with 1 method)"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "f(x) = x^2 + x + √(x+6x^2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 195,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "f (generic function with 2 methods)"
      ]
     },
     "execution_count": 195,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "f(y) = [x^2 for x in y]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 196,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[4, 9, 16, 25]\n"
     ]
    }
   ],
   "source": [
    "println(f([2,3,4,5]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 197,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "f (generic function with 2 methods)"
      ]
     },
     "execution_count": 197,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "f(y) = (x^2 for x in y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 198,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "491625\n"
     ]
    }
   ],
   "source": [
    "println(f([2,3,4,5])...)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "∑ (generic function with 1 method)"
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "∑(x,y) = x+y"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "factorial! (generic function with 1 method)"
      ]
     },
     "execution_count": 57,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "factorial!(x::Int64) = x == 1 ? one(x) : factorial!(x-1)*x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "6"
      ]
     },
     "execution_count": 59,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "factorial!(3::Int64)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "fib (generic function with 1 method)"
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fib(n::Integer) = n ≤ 2 ? one(n) : fib(n-1) + fib(n-2)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### **Anonymous/ Lamdba Expressions.**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "#1 (generic function with 1 method)"
      ]
     },
     "execution_count": 60,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x -> x^+2+3x+4"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5-element Vector{Int64}:\n",
       "  7\n",
       " 12\n",
       " 19\n",
       " 28\n",
       " 39"
      ]
     },
     "execution_count": 62,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "map(x->x^2+2x+4,[1,2,3,4,5])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5-element Vector{String}:\n",
       " \"111\"\n",
       " \"222\"\n",
       " \"333\"\n",
       " \"444\"\n",
       " \"555\""
      ]
     },
     "execution_count": 66,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "map(x-> x*x*x,[\"1\",\"2\",\"3\",\"4\",\"5\"])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "tags": []
   },
   "source": [
    "# Hands-on  **Functions**\n",
    "<div>\n",
    "     <img src=\"Handson.png\"  width=\"100\"  />  \n",
    "</div>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Generate Cincinnati word by merging letters[cinat]; you can replicate your substrings\n",
    "\n",
    "* x = 2*(\"cin\") + \"nat\"+i"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 98,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "\"cincinnati\""
      ]
     },
     "execution_count": 98,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x = string(string('c','i','n')^2 , string('n','a','t','i'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 99,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "cincinnati\n"
     ]
    }
   ],
   "source": [
    "x = \"cinat\"\n",
    "println(x[begin:3]^2*x[3:end]*x[2])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "LnbKsiN-BPa5"
   },
   "source": [
    "# **Data Structures**\n",
    "\n",
    "  * Arrays and Vectors\n",
    "  * Metrices\n",
    "  * Sets and Tuples"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Creating a 1D array/vector"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 124,
   "metadata": {
    "id": "UL31WKQiA1bm"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "4-element Vector{Int64}:\n",
       " 1\n",
       " 2\n",
       " 3\n",
       " 4"
      ]
     },
     "execution_count": 124,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Array1 = [1, 2, 3, 4]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 126,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "4-element Vector{Int64}:\n",
       " 1\n",
       " 2\n",
       " 3\n",
       " 4"
      ]
     },
     "execution_count": 126,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Array{Int64}([1, 2, 3,4])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 125,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "4-element Vector{Int64}:\n",
       " 1\n",
       " 2\n",
       " 3\n",
       " 4"
      ]
     },
     "execution_count": 125,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Vector{Int64}([1, 2, 3,4])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 110,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 2, 3, 4]\n",
      "2\n"
     ]
    }
   ],
   "source": [
    "println(Array1[begin:end])\n",
    "println(Array1[2])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Creating a 2D array\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 112,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2×3 Matrix{Int64}:\n",
       " 1  2  3\n",
       " 4  5  6"
      ]
     },
     "execution_count": 112,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Array2 = [1 2 3; 4 5 6]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 115,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 4, 2, 5, 3, 6]\n",
      "3\n",
      "3\n"
     ]
    }
   ],
   "source": [
    "println(Array2[begin:end])\n",
    "println(Array2[5])\n",
    "println(Array2[1,3])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Creating a 3D array\n",
    "## using 'cat' command"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 106,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2×2×3 Array{Int64, 3}:\n",
       "[:, :, 1] =\n",
       " 1  2\n",
       " 3  4\n",
       "\n",
       "[:, :, 2] =\n",
       " 5  6\n",
       " 7  8\n",
       "\n",
       "[:, :, 3] =\n",
       " 2  2\n",
       " 3  4"
      ]
     },
     "execution_count": 106,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Array3 = cat([1 2; 3 4], [5 6; 7 8], [2 2; 3 4], dims = 3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 119,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 3, 2, 4, 5, 7, 6, 8, 2, 3, 2, 4]\n",
      "5\n",
      "2\n"
     ]
    }
   ],
   "source": [
    "println(Array3[begin:end])\n",
    "println(Array3[5])\n",
    "println(Array3[1,2,1])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Sets"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Creating an empty set**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 136,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Empty Set: Set([3])\n"
     ]
    }
   ],
   "source": [
    "Set1 = Set(3)\n",
    "println(\"Empty Set: \", Set1)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Creating a set with Integer values**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 137,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Set([5, 4, 6, 2, 3, 1])\n"
     ]
    }
   ],
   "source": [
    "Set2 = Set([1, 2, 3, 4, 5, 2, 4, 6])\n",
    "println(Set2)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Creating a set with mixed datatypes**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 138,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Set(Any[2, \"Hello\", 3, 1, \"Cincy\"])\n",
      "Set(Any[5, 1, 4, 6, 2, \"Hello\", 3, \"Cincy\"])\n",
      "Set([3])\n"
     ]
    }
   ],
   "source": [
    "Set3 = Set([1, 2, 3, \"Hello\", \"Cincy\"])\n",
    "println(Set3)\n",
    "println(union(Set1,Set2,Set3))\n",
    "println(intersect(Set1,Set2,Set3))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Creating a Tuple"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 127,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(2, 3, 4, 5)"
      ]
     },
     "execution_count": 127,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x = (2,3,4,5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 151,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "f (generic function with 2 methods)"
      ]
     },
     "execution_count": 151,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "f(x,y,z,w) = x+y+z+w"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 150,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "71\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "14"
      ]
     },
     "execution_count": 150,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "println(f((9,53,4,5)...))\n",
    "f(x...)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Hands-on  **Data Structures**\n",
    "\n",
    "<div>\n",
    "     <img src=\"Handson.png\"  width=\"100\"  />  \n",
    "</div>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# some problems here"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# **Conditional Evaluation**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 201,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "\"whole number\""
      ]
     },
     "execution_count": 201,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x = 9\n",
    "if x >= 0\n",
    "    \"whole number\"\n",
    "else\n",
    "    \"-ve Number\"\n",
    "end"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 213,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "\"Odd Number\""
      ]
     },
     "execution_count": 213,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x = 9\n",
    "if mod(x,2) == 0\n",
    "    \"Even number\"\n",
    "elseif x==0\n",
    "     \"zero\"\n",
    "else\n",
    "     \"Odd Number\"\n",
    "end"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## **Ternary Operator**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 205,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "45\n",
      "23\n"
     ]
    }
   ],
   "source": [
    "println(3>4 ? 23 : 45)\n",
    "println(30>14 ? 23 : 45)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "ZONJNaG9xPYv"
   },
   "source": [
    "# **Control Flow**\n",
    "\n",
    "### For Loops\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 153,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1 2 3 4 5 "
     ]
    }
   ],
   "source": [
    "for x in [1,2,3,4,5]\n",
    "    print(x,\" \")\n",
    "end"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 159,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2 3 4 5 6 7 8 9 10 "
     ]
    }
   ],
   "source": [
    "for x in 2:10\n",
    "    print(x,\" \")\n",
    "end"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 164,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.0, \n",
      "0.75, \n",
      "1.5, \n",
      "2.25, \n",
      "3.0, \n"
     ]
    }
   ],
   "source": [
    "for y in range(0, stop=3, length=5)\n",
    "    print(y,\", \\n\")\n",
    "end"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Nested Statements as cartesian product"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 209,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(3, 1)(3, 2)(3, 3)(3, 4)(4, 1)(4, 2)(4, 3)(4, 4)(5, 1)(5, 2)(5, 3)(5, 4)"
     ]
    }
   ],
   "source": [
    "for i = 3:5, j = 1:4\n",
    "    print((i, j))\n",
    "end"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### While Loops\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 172,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "2\n",
      "3\n",
      "4\n",
      "5\n"
     ]
    }
   ],
   "source": [
    "x = Array{Int64}([1,2,3,4,5])\n",
    "i = 1\n",
    "while i <= length(x)\n",
    "    println(x[i])\n",
    "    i = i + 1\n",
    "end"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Iterators for Lists"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 173,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "54321"
     ]
    }
   ],
   "source": [
    "for y in Iterators.reverse(x)\n",
    "    print(y)\n",
    "end"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "WGPRsPhTAFBz"
   },
   "source": [
    "Excercises"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "PdbfL9zZC_Os"
   },
   "source": [
    "Do some computation"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "id": "X2bMWvaaDDhN"
   },
   "outputs": [],
   "source": [
    "Tax computation"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# For more on Julia visit online resources\n",
    "* [Official Documentation at julialang.org](https://docs.julialang.org/en/v1/)\n",
    "* [UC Irvin: Julia in Depth for data Scientists](http://ucidatascienceinitiative.github.io/IntroToJulia/)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "eCPv-6AIExoP"
   },
   "source": [
    "# Interesting Links and News\n",
    "\n",
    "\n",
    "*   Programming Basics\n",
    "    * Intangible Side of Programming\n",
    "      * Critical Thinking : [Coding develops CT](https://thesassway.com/what-is-critical-thinking-in-computer-science/)\n",
    "      * Mathamatics : [Computational Programming](https://www.quantamagazine.org/computing-expert-says-programmers-need-more-math-20220517/)\n",
    "      * Logical Development : [How to Think Logically](https://www.geeksforgeeks.org/i-cant-use-logic-in-programming-what-should-i-do/)\n",
    "      * Art of articulating your mind : [putting thoughts into words](https://milesberry.net/2021/11/practical-programming/)\n",
    "    * Tangible Side of Programming\n",
    "      * Syntax Learning : [Grammer](https://pgrandinetti.github.io/compilers/page/what-is-a-programming-language-grammar/#:~:text=A%20Programming%20Language%20Grammar%20is,statements%20(also%20called%20sentences).)\n",
    "      * Programming Constructs : [Sentence Formation](https://cgi.csc.liv.ac.uk/~frans/OldLectures/2CS45/progCons/progCons.html)\n",
    "      * Program Flow : [Control Flow](https://en.wikipedia.org/wiki/Control_flow)\n",
    "      * Programming Features : [Writing Style](https://scoutapm.com/blog/functional-vs-procedural-vs-oop)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "x5nRI3OqFKhP"
   },
   "source": [
    "# Upcoming Julia Workshop\n",
    "* **Julia for Mathematician : Functions and Plots**\n",
    "* **Data Visualization with Julia**"
   ]
  }
 ],
 "metadata": {
  "colab": {
   "collapsed_sections": [],
   "name": "Julia.ipynb",
   "provenance": []
  },
  "kernelspec": {
   "display_name": "Julia 1.7.2",
   "language": "julia",
   "name": "julia-1.7"
  },
  "language_info": {
   "file_extension": ".jl",
   "mimetype": "application/julia",
   "name": "julia",
   "version": "1.7.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
