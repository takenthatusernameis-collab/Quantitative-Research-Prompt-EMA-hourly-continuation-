# EMA Hourly Continuation — JUP/USDT P8_34

**Symbol:** JUP/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 699 |
| net_profit_factor | 0.7928 |
| net_win_rate | 0.5007 |
| gross_profit_factor | 0.9924 |
| gross_win_rate | 0.5007 |
| sharpe_ratio | -1.8601 |
| sortino_ratio | -0.7048 |
| max_drawdown | 0.5762 |
| cagr | -0.2780 |
| net_avg_win | 61.0714 |
| net_avg_loss | -77.2551 |
| avg_hold_time_bars | 9.0572 |
| exposure | 0.2878 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
