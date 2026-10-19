# EMA Hourly Continuation — IOTA/USDT P55_100

**Symbol:** IOTA/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 622 |
| net_profit_factor | 0.4375 |
| net_win_rate | 0.4341 |
| gross_profit_factor | 0.7696 |
| gross_win_rate | 0.4421 |
| sharpe_ratio | -5.9742 |
| sortino_ratio | -2.1027 |
| max_drawdown | 0.9268 |
| cagr | -0.6384 |
| net_avg_win | 26.5674 |
| net_avg_loss | -46.5797 |
| avg_hold_time_bars | 5.2701 |
| exposure | 0.1490 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
