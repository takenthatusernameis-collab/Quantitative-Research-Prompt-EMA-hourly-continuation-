# EMA Hourly Continuation — AAVE/USDT P20_34

**Symbol:** AAVE/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 270 |
| net_profit_factor | 0.7140 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9959 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.7032 |
| sortino_ratio | -0.4022 |
| max_drawdown | 0.3752 |
| cagr | -0.1678 |
| net_avg_win | 68.3609 |
| net_avg_loss | -95.7395 |
| avg_hold_time_bars | 5.7963 |
| exposure | 0.0711 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
