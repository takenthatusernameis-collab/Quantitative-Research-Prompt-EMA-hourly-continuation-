# EMA Hourly Continuation — G/USDT P50_144

**Symbol:** G/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 413 |
| net_profit_factor | 0.5179 |
| net_win_rate | 0.4504 |
| gross_profit_factor | 0.8514 |
| gross_win_rate | 0.4649 |
| sharpe_ratio | -4.2655 |
| sortino_ratio | -1.3250 |
| max_drawdown | 0.7620 |
| cagr | -0.4641 |
| net_avg_win | 42.8523 |
| net_avg_loss | -67.7926 |
| avg_hold_time_bars | 13.8063 |
| exposure | 0.2998 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
