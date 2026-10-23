# EMA Hourly Continuation — API3/USDT P50_100

**Symbol:** API3/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 632 |
| net_profit_factor | 0.5768 |
| net_win_rate | 0.4589 |
| gross_profit_factor | 0.9300 |
| gross_win_rate | 0.4778 |
| sharpe_ratio | -4.5835 |
| sortino_ratio | -1.6378 |
| max_drawdown | 0.8692 |
| cagr | -0.5370 |
| net_avg_win | 40.2017 |
| net_avg_loss | -59.0999 |
| avg_hold_time_bars | 6.8987 |
| exposure | 0.1982 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
