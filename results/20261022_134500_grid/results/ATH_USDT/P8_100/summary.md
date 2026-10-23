# EMA Hourly Continuation — ATH/USDT P8_100

**Symbol:** ATH/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 658 |
| net_profit_factor | 0.6749 |
| net_win_rate | 0.4878 |
| gross_profit_factor | 0.9803 |
| gross_win_rate | 0.4924 |
| sharpe_ratio | -3.4182 |
| sortino_ratio | -1.2685 |
| max_drawdown | 0.7740 |
| cagr | -0.4590 |
| net_avg_win | 49.4545 |
| net_avg_loss | -69.7976 |
| avg_hold_time_bars | 20.3191 |
| exposure | 0.6481 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
