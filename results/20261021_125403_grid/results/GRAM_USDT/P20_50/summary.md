# EMA Hourly Continuation — GRAM/USDT P20_50

**Symbol:** GRAM/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 430 |
| net_profit_factor | 0.6510 |
| net_win_rate | 0.4814 |
| gross_profit_factor | 0.9401 |
| gross_win_rate | 0.4814 |
| sharpe_ratio | -2.8290 |
| sortino_ratio | -0.8406 |
| max_drawdown | 0.6342 |
| cagr | -0.3186 |
| net_avg_win | 55.7184 |
| net_avg_loss | -79.4511 |
| avg_hold_time_bars | 7.9767 |
| exposure | 0.1559 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
