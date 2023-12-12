The categorization of bugs utilized in this study builds upon the framework set by [Web3Bugs](https://github.com/ZhangZhuoSJTU/Web3Bugs/blob/main/docs/standard.md). However, we've introduced minor modifications to align with the specific requirements of our evaluation process.

Each bug category is briefly explained first. This is followed by a more detailed subdivision of each category to provide a comprehensive understanding of the bugs we encountered during the course of our research.

Please note that our modifications to the original Web3Bugs classification serve to enhance the precision and relevance of our findings. These changes were necessitated by the unique nature of our evaluation criteria and the specificities of the bugs we investigated.

## Bug Categorization
Different with the machine auditable bugs (MABs) which can be detected through simple, general oracles and do not require an in-depth understanding of the code semantics, machine unditable bugs (MUBs) present a more complex case. MUBs necessitate the use of advanced semantic oracles for detection because they originate from discrepancies between the code implementation and the intended business model. They are categorized into the following six categories in this work and may be subject to modifications in the future. These adaptations will be influenced by the performance of the Language Learning Model (LLM) in response to different prompts, as we continue to refine our understanding and detection capabilities of MUBs.

+ __Price Oracle Manipulation (C1)__:
Price oracles are entities that supply external price data into the blockchain which themselves cannot access external data. This function is crucial for many  decentralized applications (dApps) as they usually require price information to drive their business models. Typical manipulation practices include Automated Market Maker (AMM) interference and sandwich attacks, among others.
Detecting such vulnerabilities is challenging, as per [Zhang](https://github.com/ZhangZhuoSJTU/Web3Bugs/blob/main/papers/icse23.pdf), where they found 75% of such bugs were identified by only a single individual or group. 


+ __Erroneous Accounting (C2)__:
Erroneous accounting involves incorrect implementation of business logic in smart contracts, resulting in seemingly minor bugs. While initially trivial, these bugs, including rounding, precision, and order of operation errors, can compound due to the repetitive nature of transactions, leading to significant losses. About 59% of such bugs are identified by only a single individual or group, indicating the challenge in their detection.


+ __Improper Access Control (C3)__:
Improper access control refers to situations where a user is able to perform actions or access data that they shouldn't be able to. They can lead to unauthorized actions, security breaches, and even loss of funds.



+ __Erroneous State Updates (C4)__:
The "state" of a smart contract refers to the stored data that can be modified by transactions. A smart contract's state is updated as a result of function calls and transactions.  Erroneous state updates refer to updates that happen incorrectly due to programming mistakes or attacks. About 53% of such bugs are identified by a single individual or group.



+ __Atomicity Violations (C5)__:
Atomicity is a principle taken from database systems, where it denotes a property of transactions: an atomic transaction is one that is executed in its entirety or not at all. This means that if an operation within the transaction fails, the entire transaction is rolled back, ensuring the consistency of the data. In the context of blockchain smart contracts, an atomicity violation can occur when a transaction (i.e., a series of operations within a smart contract) is partially completed, resulting in an inconsistent or incorrect state. This can be particularly problematic given the immutable nature of blockchains - once data is written to the chain, it cannot be modified or erased.

+ __Implementation Bugs (C6)__:
Implementation bugs do not have a general pattern, they randomly show in the contracts and hard to detect.


## Extended Bug Categorization with Subcategories
We further extend the six main categories with subcategories, which provide a more nuanced understanding of the bugs that fall under each category, with each subcategory addressing a unique form or manifestation of the parent category.

+ __C1__: Price oracle manipulation.
    + __S1-1__: AMM price oracle manipulation.
    + __S1-2__: Sandwich attack.
    + __S1-3__: Non-AMM price oracle manipulation.
+ __C2__: Erroneous accounting.
    + __S6-1__: Incorrect calculating order.
    + __S6-2__: Returning an unexpected value that deviates from the expected semantics specified for the contract.
    + __S6-3__: Calculations performed with incorrect numbers (e.g., `x = a + b` ==> `x = a + c`).
    + __S6-4__: Other accounting errors (e.g., `x = a + b` ==> `x = a - b`).    
+ __C3__: Improper access control.
    + __S2-1__: ID can be arbitrarily set by users or lack of ID validation. ID can also be a project-specified variable (e.g., hash) or an address.
    + __S2-2__: Shared resource (e.g., token) without proper locks.
    + __S2-3__: ID uniqueness violation (i.e., an ID should be unique but it is not).
    + __S5-1__: Users can update privileged state variables arbitrarily (caused by lack of ID-unrelated input sanitization).
    + __S5-2__: Users can invoke some functions at a time they should not be able to do so.
    + __S5-3__: Privileged functions can be called by anyone or at any time.
+ __C4__: Erroneous state updates.
    + __S3-1__: Missing state update.
    + __S3-2__: Incorrect state updates, e.g., a state update that should not be there.
+ __C5__: Broken business models.
    + __S4-1__: Lack of proper locks for a business flow consisting of multiple transactions.
    + __SE-1__: Unexpected function invocation sequences (e.g., external calls to dependent contracts).
    + __SE-2__: Unexpected environment or contract conditions (e.g., ChainLink returning outdated data or significant slippage occurring).
    + __SE-3__: A given function is invoked multiple times unexpectedly.
    + __SE-4__: Unexpected function arguments.
+ __C6__: Contract implementation-specific bugs.


### Bugs with Simple and General Testing Oracles

These kinds of bugs are also derived from [Web3Bugs](https://github.com/ZhangZhuoSJTU/Web3Bugs/blob/main/docs/standard.md), which can be detected using simple and general oracles and do not require an in-depth understanding of the code semantics. We update several ones according to our requirement.

+ __L1__: Reentrancy.
+ __L2__: Rounding issues or precision loss.
+ __L3__: Bugs that are caused by using uninitialized variables.
+ __L4__: Bugs that are caused by exceeding the gas limitation.
+ __L5__: Storage collision and confusion between proxy and implementation.
+ __L6__: Arbitrary external function call.
+ __L7__: Integer overflow and underflow.
+ __L8__: Unchecked return value by low-level call and other function calls.
+ __L9__: Bugs that are caused by writing to memory that does not apply to the storage.
+ __LA__: Cryptographic issues.
+ __LB__: Using `tx.origin`.
+ __LC__: Using `timestamp`.