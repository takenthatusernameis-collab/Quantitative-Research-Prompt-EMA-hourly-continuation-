# EMA Hourly Continuation — ANKR/USDT P26_200

**Symbol:** ANKR/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 310 |
| net_profit_factor | 0.7798 |
| net_win_rate | 0.4968 |
| gross_profit_factor | 0.9882 |
| gross_win_rate | 0.4968 |
| sharpe_ratio | -1.3917 |
| sortino_ratio | -0.3501 |
| max_drawdown | 0.3535 |
| cagr | -0.1506 |
| net_avg_win | 77.3347 |
| net_avg_loss | -97.9012 |
| avg_hold_time_bars | 43.9935 |
| exposure | 0.6199 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
