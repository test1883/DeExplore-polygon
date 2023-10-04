const Transaction = require("../models/transactionModel");

const getTransactions = async (req, res) => {
    const { from } = req.body;
    const fromTxn = await Transaction.find({ from }).sort({ at: -1 });
    const toTxn = await Transaction.find({ to: from }).sort({ at: -1 });
    res.status(200).send({ from: fromTxn, to: toTxn });
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
