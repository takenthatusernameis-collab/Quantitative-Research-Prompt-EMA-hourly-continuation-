# EMA Hourly Continuation — MINA/USDT P26_55

**Symbol:** MINA/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 924 |
| net_profit_factor | 0.5657 |
| net_win_rate | 0.4708 |
| gross_profit_factor | 1.0254 |
| gross_win_rate | 0.4892 |
| sharpe_ratio | -6.0567 |
| sortino_ratio | -2.6044 |
| max_drawdown | 0.9614 |
| cagr | -0.7143 |
| net_avg_win | 28.6573 |
| net_avg_loss | -45.0632 |
| avg_hold_time_bars | 5.0379 |
| exposure | 0.2116 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
