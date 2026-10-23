# EMA Hourly Continuation — BLZ/USDT P21_100

**Symbol:** BLZ/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 736 |
| net_profit_factor | 0.5750 |
| net_win_rate | 0.4253 |
| gross_profit_factor | 0.8754 |
| gross_win_rate | 0.4348 |
| sharpe_ratio | -5.9281 |
| sortino_ratio | -2.2568 |
| max_drawdown | 0.9379 |
| cagr | -0.6615 |
| net_avg_win | 40.4137 |
| net_avg_loss | -52.0069 |
| avg_hold_time_bars | 12.7351 |
| exposure | 0.4242 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
