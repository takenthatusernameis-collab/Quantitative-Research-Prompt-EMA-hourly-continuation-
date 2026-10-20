# EMA Hourly Continuation — REZ/USDT P8_20

**Symbol:** REZ/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1556 |
| net_profit_factor | 0.5920 |
| net_win_rate | 0.4634 |
| gross_profit_factor | 1.0452 |
| gross_win_rate | 0.4769 |
| sharpe_ratio | -8.4647 |
| sortino_ratio | -4.7375 |
| max_drawdown | 0.9967 |
| cagr | -0.9008 |
| net_avg_win | 20.0549 |
| net_avg_loss | -29.2535 |
| avg_hold_time_bars | 3.2449 |
| exposure | 0.2329 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
