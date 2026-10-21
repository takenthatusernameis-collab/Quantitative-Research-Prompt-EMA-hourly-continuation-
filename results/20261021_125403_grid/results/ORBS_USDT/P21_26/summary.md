# EMA Hourly Continuation — ORBS/USDT P21_26

**Symbol:** ORBS/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 314 |
| net_profit_factor | 0.3803 |
| net_win_rate | 0.3503 |
| gross_profit_factor | 0.6332 |
| gross_win_rate | 0.3535 |
| sharpe_ratio | -5.8816 |
| sortino_ratio | -1.4958 |
| max_drawdown | 0.8330 |
| cagr | -0.5069 |
| net_avg_win | 46.3345 |
| net_avg_loss | -65.6994 |
| avg_hold_time_bars | 5.9873 |
| exposure | 0.0855 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
