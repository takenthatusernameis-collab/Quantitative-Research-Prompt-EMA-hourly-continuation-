# EMA Hourly Continuation — XPR/USDT P8_89

**Symbol:** XPR/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 869 |
| net_profit_factor | 0.4907 |
| net_win_rate | 0.4338 |
| gross_profit_factor | 0.8005 |
| gross_win_rate | 0.4384 |
| sharpe_ratio | -6.8721 |
| sortino_ratio | -2.8291 |
| max_drawdown | 0.9722 |
| cagr | -0.7568 |
| net_avg_win | 24.8231 |
| net_avg_loss | -38.7625 |
| avg_hold_time_bars | 14.1519 |
| exposure | 0.5590 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
