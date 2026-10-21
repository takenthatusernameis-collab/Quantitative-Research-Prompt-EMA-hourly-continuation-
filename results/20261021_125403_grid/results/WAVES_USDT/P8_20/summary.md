# EMA Hourly Continuation — WAVES/USDT P8_20

**Symbol:** WAVES/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 535 |
| net_profit_factor | 0.6224 |
| net_win_rate | 0.4860 |
| gross_profit_factor | 0.9473 |
| gross_win_rate | 0.4879 |
| sharpe_ratio | -3.5452 |
| sortino_ratio | -1.1767 |
| max_drawdown | 0.7489 |
| cagr | -0.4171 |
| net_avg_win | 47.0397 |
| net_avg_loss | -71.4608 |
| avg_hold_time_bars | 5.7477 |
| exposure | 0.1398 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
