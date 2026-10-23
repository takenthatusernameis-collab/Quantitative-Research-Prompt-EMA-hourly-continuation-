# EMA Hourly Continuation — CELR/USDT P55_89

**Symbol:** CELR/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 663 |
| net_profit_factor | 0.4864 |
| net_win_rate | 0.4465 |
| gross_profit_factor | 0.8797 |
| gross_win_rate | 0.4721 |
| sharpe_ratio | -5.6149 |
| sortino_ratio | -2.0358 |
| max_drawdown | 0.9190 |
| cagr | -0.6264 |
| net_avg_win | 29.3292 |
| net_avg_loss | -48.6299 |
| avg_hold_time_bars | 4.6727 |
| exposure | 0.1402 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
