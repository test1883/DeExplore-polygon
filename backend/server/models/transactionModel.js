const mongoose = require("mongoose");

const Schema = mongoose.Schema;

const transactionSchema = new Schema({
    amount: {
        type: Number,
        required: true,
    },
    type: {
        type: String,
        enum: [
            "Deposit",
            "Withdraw",
            "Face Transaction",
            "Pin Transaction",
            "App Transfer",
            "Transfer",
        ],
        required: true,
    },
    from: {
        type: String,
        enum: [/^0x[a-fA-F0-9]{40}$/g],
        required: true,
    },
    to: {
        type: String,
        enum: [/^0x[a-fA-F0-9]{40}$/g],
    },
    at: {
        type: Number,
        required: true,
    },
    by: {
        type: String,
        required: true,
    },
    category: {
        type: String,
    },
});

module.exports = mongoose.model("Transaction", transactionSchema);
