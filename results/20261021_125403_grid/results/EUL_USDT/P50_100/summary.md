# EMA Hourly Continuation — EUL/USDT P50_100

**Symbol:** EUL/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 322 |
| net_profit_factor | 0.6385 |
| net_win_rate | 0.4596 |
| gross_profit_factor | 0.8434 |
| gross_win_rate | 0.4596 |
| sharpe_ratio | -2.4369 |
| sortino_ratio | -0.6224 |
| max_drawdown | 0.5290 |
| cagr | -0.2481 |
| net_avg_win | 61.0183 |
| net_avg_loss | -81.2848 |
| avg_hold_time_bars | 10.4348 |
| exposure | 0.1527 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
