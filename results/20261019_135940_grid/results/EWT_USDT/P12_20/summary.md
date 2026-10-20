# EMA Hourly Continuation — EWT/USDT P12_20

**Symbol:** EWT/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1279 |
| net_profit_factor | 0.2448 |
| net_win_rate | 0.3096 |
| gross_profit_factor | 0.5992 |
| gross_win_rate | 0.3565 |
| sharpe_ratio | -16.4481 |
| sortino_ratio | -8.5918 |
| max_drawdown | 1.0000 |
| cagr | -0.9904 |
| net_avg_win | 8.1842 |
| net_avg_loss | -14.9953 |
| avg_hold_time_bars | 2.5160 |
| exposure | 0.1463 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
