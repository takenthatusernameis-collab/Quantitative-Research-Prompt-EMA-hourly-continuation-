# EMA Hourly Continuation — DOT/USDT P34_55

**Symbol:** DOT/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 845 |
| net_profit_factor | 0.4130 |
| net_win_rate | 0.4533 |
| gross_profit_factor | 0.9111 |
| gross_win_rate | 0.4651 |
| sharpe_ratio | -8.0451 |
| sortino_ratio | -3.3002 |
| max_drawdown | 0.9862 |
| cagr | -0.8152 |
| net_avg_win | 18.1091 |
| net_avg_loss | -36.3456 |
| avg_hold_time_bars | 3.0414 |
| exposure | 0.1168 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
