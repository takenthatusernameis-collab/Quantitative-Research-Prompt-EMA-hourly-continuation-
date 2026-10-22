# EMA Hourly Continuation — XDC/USDT P34_50

**Symbol:** XDC/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 979 |
| net_profit_factor | 0.1376 |
| net_win_rate | 0.3473 |
| gross_profit_factor | 0.5481 |
| gross_win_rate | 0.4239 |
| sharpe_ratio | -14.0342 |
| sortino_ratio | -6.5093 |
| max_drawdown | 0.9999 |
| cagr | -0.9707 |
| net_avg_win | 4.6919 |
| net_avg_loss | -18.1437 |
| avg_hold_time_bars | 2.9510 |
| exposure | 0.1313 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
