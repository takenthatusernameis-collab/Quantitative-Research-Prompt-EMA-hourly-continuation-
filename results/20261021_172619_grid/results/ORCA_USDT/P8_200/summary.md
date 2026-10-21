# EMA Hourly Continuation — ORCA/USDT P8_200

**Symbol:** ORCA/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 290 |
| net_profit_factor | 0.8005 |
| net_win_rate | 0.4931 |
| gross_profit_factor | 0.9689 |
| gross_win_rate | 0.4966 |
| sharpe_ratio | -1.1526 |
| sortino_ratio | -0.2798 |
| max_drawdown | 0.3373 |
| cagr | -0.1226 |
| net_avg_win | 78.5586 |
| net_avg_loss | -95.4613 |
| avg_hold_time_bars | 61.5241 |
| exposure | 0.8110 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
