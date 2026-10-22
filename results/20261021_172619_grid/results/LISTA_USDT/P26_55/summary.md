# EMA Hourly Continuation — LISTA/USDT P26_55

**Symbol:** LISTA/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 493 |
| net_profit_factor | 0.6578 |
| net_win_rate | 0.4584 |
| gross_profit_factor | 0.8607 |
| gross_win_rate | 0.4584 |
| sharpe_ratio | -3.2090 |
| sortino_ratio | -1.0514 |
| max_drawdown | 0.6820 |
| cagr | -0.3832 |
| net_avg_win | 57.5281 |
| net_avg_loss | -74.0238 |
| avg_hold_time_bars | 7.7343 |
| exposure | 0.1864 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
