# EMA Hourly Continuation — POL/USDT P12_21

**Symbol:** POL/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 291 |
| net_profit_factor | 0.5523 |
| net_win_rate | 0.4536 |
| gross_profit_factor | 0.8024 |
| gross_win_rate | 0.4536 |
| sharpe_ratio | -2.9269 |
| sortino_ratio | -0.7142 |
| max_drawdown | 0.5847 |
| cagr | -0.2787 |
| net_avg_win | 52.3191 |
| net_avg_loss | -78.6377 |
| avg_hold_time_bars | 5.5120 |
| exposure | 0.0729 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
