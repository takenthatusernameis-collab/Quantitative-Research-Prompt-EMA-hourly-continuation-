# EMA Hourly Continuation — XTZ/USDT P144_200

**Symbol:** XTZ/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 439 |
| net_profit_factor | 0.3808 |
| net_win_rate | 0.4419 |
| gross_profit_factor | 0.8329 |
| gross_win_rate | 0.4601 |
| sharpe_ratio | -5.6945 |
| sortino_ratio | -1.6921 |
| max_drawdown | 0.8813 |
| cagr | -0.5706 |
| net_avg_win | 27.9016 |
| net_avg_loss | -58.0239 |
| avg_hold_time_bars | 3.9590 |
| exposure | 0.0790 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
