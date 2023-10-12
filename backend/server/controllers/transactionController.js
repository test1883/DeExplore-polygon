const Transaction = require("../models/transactionModel");

const getTransactions = async (req, res) => {
    const { from } = req.body;
    const fromTxn = await Transaction.find({ from }).sort({ at: -1 });
    const toTxn = await Transaction.find({ to: from }).sort({ at: -1 });
    for (let i = 0; i < fromTxn.length; i++) {
        fromTxn[i].txn = "from";
    }
    for (let i = 0; i < toTxn.length; i++) {
        toTxn[i].txn = "to";
    }
    const arr = [...fromTxn, ...toTxn].sort(function compare(a, b) {
        if (a.at < b.at) {
            return -1;
        }
        if (a.at > b.at) {
            return 1;
        }
        // a must be equal to b
        return 0;
    });
    res.status(200).send(arr);
};

const addTransaction = async (req, res) => {
    const { amount, from, to, by, type, category } = req.body;
    const transaction = await Transaction.create({
        amount,
        from,
        to,
        by,
        type,
        at: Date.now(),
        category,
    });
    res.status(200).send(transaction);
};

module.exports = { getTransactions, addTransaction };
