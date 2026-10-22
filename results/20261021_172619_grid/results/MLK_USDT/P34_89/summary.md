# EMA Hourly Continuation — MLK/USDT P34_89

**Symbol:** MLK/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 404 |
| net_profit_factor | 0.3852 |
| net_win_rate | 0.3416 |
| gross_profit_factor | 0.5489 |
| gross_win_rate | 0.3441 |
| sharpe_ratio | -5.9480 |
| sortino_ratio | -1.6901 |
| max_drawdown | 0.8665 |
| cagr | -0.5467 |
| net_avg_win | 39.2273 |
| net_avg_loss | -52.8342 |
| avg_hold_time_bars | 10.8663 |
| exposure | 0.1987 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
