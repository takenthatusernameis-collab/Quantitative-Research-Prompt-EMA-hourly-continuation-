# EMA Hourly Continuation — APE/USDT P21_200

**Symbol:** APE/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 306 |
| net_profit_factor | 0.7638 |
| net_win_rate | 0.4804 |
| gross_profit_factor | 0.9012 |
| gross_win_rate | 0.4804 |
| sharpe_ratio | -1.3448 |
| sortino_ratio | -0.3351 |
| max_drawdown | 0.3397 |
| cagr | -0.1441 |
| net_avg_win | 71.1164 |
| net_avg_loss | -86.0864 |
| avg_hold_time_bars | 42.4477 |
| exposure | 0.5904 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
