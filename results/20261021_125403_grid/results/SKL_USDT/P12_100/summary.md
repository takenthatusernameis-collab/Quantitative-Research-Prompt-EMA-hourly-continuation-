# EMA Hourly Continuation — SKL/USDT P12_100

**Symbol:** SKL/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 457 |
| net_profit_factor | 0.8819 |
| net_win_rate | 0.5142 |
| gross_profit_factor | 1.0607 |
| gross_win_rate | 0.5142 |
| sharpe_ratio | -0.8995 |
| sortino_ratio | -0.2762 |
| max_drawdown | 0.4412 |
| cagr | -0.1227 |
| net_avg_win | 89.0509 |
| net_avg_loss | -106.8836 |
| avg_hold_time_bars | 28.4967 |
| exposure | 0.5920 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
