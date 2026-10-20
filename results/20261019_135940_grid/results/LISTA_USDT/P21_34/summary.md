# EMA Hourly Continuation — LISTA/USDT P21_34

**Symbol:** LISTA/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 979 |
| net_profit_factor | 0.5049 |
| net_win_rate | 0.4321 |
| gross_profit_factor | 0.9102 |
| gross_win_rate | 0.4525 |
| sharpe_ratio | -8.3200 |
| sortino_ratio | -3.8371 |
| max_drawdown | 0.9874 |
| cagr | -0.8438 |
| net_avg_win | 23.7959 |
| net_avg_loss | -35.8536 |
| avg_hold_time_bars | 3.3289 |
| exposure | 0.1594 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
