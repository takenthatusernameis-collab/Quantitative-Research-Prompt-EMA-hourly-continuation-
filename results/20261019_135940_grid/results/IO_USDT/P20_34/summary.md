# EMA Hourly Continuation — IO/USDT P20_34

**Symbol:** IO/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1057 |
| net_profit_factor | 0.4701 |
| net_win_rate | 0.4494 |
| gross_profit_factor | 0.8085 |
| gross_win_rate | 0.4598 |
| sharpe_ratio | -8.1644 |
| sortino_ratio | -3.8680 |
| max_drawdown | 0.9890 |
| cagr | -0.8523 |
| net_avg_win | 18.4728 |
| net_avg_loss | -32.0697 |
| avg_hold_time_bars | 2.6528 |
| exposure | 0.1357 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
