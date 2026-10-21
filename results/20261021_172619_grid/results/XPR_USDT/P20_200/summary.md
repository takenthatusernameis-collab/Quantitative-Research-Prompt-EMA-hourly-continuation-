# EMA Hourly Continuation — XPR/USDT P20_200

**Symbol:** XPR/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 285 |
| net_profit_factor | 0.8357 |
| net_win_rate | 0.5053 |
| gross_profit_factor | 0.9972 |
| gross_win_rate | 0.5053 |
| sharpe_ratio | -0.8505 |
| sortino_ratio | -0.2054 |
| max_drawdown | 0.2368 |
| cagr | -0.0919 |
| net_avg_win | 75.9797 |
| net_avg_loss | -92.8524 |
| avg_hold_time_bars | 44.6386 |
| exposure | 0.5783 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
