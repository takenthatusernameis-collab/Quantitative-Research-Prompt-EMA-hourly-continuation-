# EMA Hourly Continuation — GMT/USDT P12_100

**Symbol:** GMT/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 471 |
| net_profit_factor | 0.7586 |
| net_win_rate | 0.4798 |
| gross_profit_factor | 0.9273 |
| gross_win_rate | 0.4798 |
| sharpe_ratio | -1.9352 |
| sortino_ratio | -0.5986 |
| max_drawdown | 0.5246 |
| cagr | -0.2413 |
| net_avg_win | 69.5386 |
| net_avg_loss | -84.5620 |
| avg_hold_time_bars | 26.4225 |
| exposure | 0.5657 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
