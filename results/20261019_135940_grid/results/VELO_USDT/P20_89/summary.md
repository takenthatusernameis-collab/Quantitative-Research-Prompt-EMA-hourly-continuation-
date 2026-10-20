# EMA Hourly Continuation — VELO/USDT P20_89

**Symbol:** VELO/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 789 |
| net_profit_factor | 0.6989 |
| net_win_rate | 0.4930 |
| gross_profit_factor | 0.9765 |
| gross_win_rate | 0.4968 |
| sharpe_ratio | -3.3339 |
| sortino_ratio | -1.3204 |
| max_drawdown | 0.8079 |
| cagr | -0.4656 |
| net_avg_win | 47.3110 |
| net_avg_loss | -65.8272 |
| avg_hold_time_bars | 10.4575 |
| exposure | 0.3750 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
