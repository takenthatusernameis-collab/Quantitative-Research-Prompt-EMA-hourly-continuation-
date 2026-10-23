# EMA Hourly Continuation — DOGS/USDT P12_26

**Symbol:** DOGS/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1261 |
| net_profit_factor | 0.4061 |
| net_win_rate | 0.4171 |
| gross_profit_factor | 0.7428 |
| gross_win_rate | 0.4346 |
| sharpe_ratio | -11.2083 |
| sortino_ratio | -6.0677 |
| max_drawdown | 0.9986 |
| cagr | -0.9522 |
| net_avg_win | 12.9817 |
| net_avg_loss | -22.8762 |
| avg_hold_time_bars | 2.6225 |
| exposure | 0.1754 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
