# EMA Hourly Continuation — FIDA/USDT P12_26

**Symbol:** FIDA/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1339 |
| net_profit_factor | 0.3904 |
| net_win_rate | 0.4354 |
| gross_profit_factor | 0.7578 |
| gross_win_rate | 0.4548 |
| sharpe_ratio | -9.6258 |
| sortino_ratio | -4.9607 |
| max_drawdown | 0.9979 |
| cagr | -0.9137 |
| net_avg_win | 10.9639 |
| net_avg_loss | -21.6551 |
| avg_hold_time_bars | 3.8051 |
| exposure | 0.2306 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
