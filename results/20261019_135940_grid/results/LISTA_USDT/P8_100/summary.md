# EMA Hourly Continuation — LISTA/USDT P8_100

**Symbol:** LISTA/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 617 |
| net_profit_factor | 0.6973 |
| net_win_rate | 0.4846 |
| gross_profit_factor | 0.9613 |
| gross_win_rate | 0.4911 |
| sharpe_ratio | -2.8390 |
| sortino_ratio | -1.0268 |
| max_drawdown | 0.6862 |
| cagr | -0.3868 |
| net_avg_win | 52.4568 |
| net_avg_loss | -70.7295 |
| avg_hold_time_bars | 21.1767 |
| exposure | 0.6389 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
