# EMA Hourly Continuation — ORBS/USDT P8_89

**Symbol:** ORBS/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 575 |
| net_profit_factor | 0.6940 |
| net_win_rate | 0.4661 |
| gross_profit_factor | 0.9190 |
| gross_win_rate | 0.4661 |
| sharpe_ratio | -3.2548 |
| sortino_ratio | -1.1092 |
| max_drawdown | 0.7308 |
| cagr | -0.3999 |
| net_avg_win | 61.1441 |
| net_avg_loss | -76.9160 |
| avg_hold_time_bars | 23.5722 |
| exposure | 0.6161 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
