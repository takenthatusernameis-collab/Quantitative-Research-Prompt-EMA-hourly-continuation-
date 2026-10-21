# EMA Hourly Continuation — HTX/USDT P8_144

**Symbol:** HTX/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 368 |
| net_profit_factor | 0.6231 |
| net_win_rate | 0.4647 |
| gross_profit_factor | 0.9598 |
| gross_win_rate | 0.4701 |
| sharpe_ratio | -3.5142 |
| sortino_ratio | -0.9596 |
| max_drawdown | 0.7171 |
| cagr | -0.3636 |
| net_avg_win | 65.7569 |
| net_avg_loss | -91.6080 |
| avg_hold_time_bars | 43.7391 |
| exposure | 0.7284 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
