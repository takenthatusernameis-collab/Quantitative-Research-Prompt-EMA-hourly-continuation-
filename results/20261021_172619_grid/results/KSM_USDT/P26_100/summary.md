# EMA Hourly Continuation — KSM/USDT P26_100

**Symbol:** KSM/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 437 |
| net_profit_factor | 0.7909 |
| net_win_rate | 0.5103 |
| gross_profit_factor | 1.0316 |
| gross_win_rate | 0.5103 |
| sharpe_ratio | -1.5263 |
| sortino_ratio | -0.4578 |
| max_drawdown | 0.4407 |
| cagr | -0.1902 |
| net_avg_win | 69.7613 |
| net_avg_loss | -91.9152 |
| avg_hold_time_bars | 18.3730 |
| exposure | 0.3650 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
