# EMA Hourly Continuation — ANKR/USDT P8_34

**Symbol:** ANKR/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1296 |
| net_profit_factor | 0.4897 |
| net_win_rate | 0.4344 |
| gross_profit_factor | 0.9171 |
| gross_win_rate | 0.4552 |
| sharpe_ratio | -9.2344 |
| sortino_ratio | -4.6921 |
| max_drawdown | 0.9970 |
| cagr | -0.9008 |
| net_avg_win | 16.9941 |
| net_avg_loss | -26.6541 |
| avg_hold_time_bars | 6.5610 |
| exposure | 0.3865 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
