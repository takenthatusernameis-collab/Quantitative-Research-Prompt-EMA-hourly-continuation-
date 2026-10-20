# EMA Hourly Continuation — WEMIX/USDT P8_89

**Symbol:** WEMIX/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1215 |
| net_profit_factor | 0.3310 |
| net_win_rate | 0.3160 |
| gross_profit_factor | 0.5525 |
| gross_win_rate | 0.3300 |
| sharpe_ratio | -13.2946 |
| sortino_ratio | -6.5802 |
| max_drawdown | 0.9998 |
| cagr | -0.9631 |
| net_avg_win | 12.8799 |
| net_avg_loss | -17.9824 |
| avg_hold_time_bars | 10.9514 |
| exposure | 0.6048 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
