# EMA Hourly Continuation — EWT/USDT P8_55

**Symbol:** EWT/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 625 |
| net_profit_factor | 0.6399 |
| net_win_rate | 0.4448 |
| gross_profit_factor | 0.7942 |
| gross_win_rate | 0.4448 |
| sharpe_ratio | -3.4551 |
| sortino_ratio | -1.2234 |
| max_drawdown | 0.7596 |
| cagr | -0.4306 |
| net_avg_win | 48.3861 |
| net_avg_loss | -60.5783 |
| avg_hold_time_bars | 12.6000 |
| exposure | 0.3580 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
