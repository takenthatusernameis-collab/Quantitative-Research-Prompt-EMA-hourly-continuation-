# EMA Hourly Continuation — CWEB/USDT P8_144

**Symbol:** CWEB/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 324 |
| net_profit_factor | 0.6068 |
| net_win_rate | 0.4537 |
| gross_profit_factor | 0.9099 |
| gross_win_rate | 0.4722 |
| sharpe_ratio | -3.0884 |
| sortino_ratio | -0.7753 |
| max_drawdown | 0.6371 |
| cagr | -0.3203 |
| net_avg_win | 65.1825 |
| net_avg_loss | -89.2092 |
| avg_hold_time_bars | 53.9475 |
| exposure | 0.7945 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
