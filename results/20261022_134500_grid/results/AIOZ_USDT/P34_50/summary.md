# EMA Hourly Continuation — AIOZ/USDT P34_50

**Symbol:** AIOZ/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 994 |
| net_profit_factor | 0.5325 |
| net_win_rate | 0.4296 |
| gross_profit_factor | 0.9350 |
| gross_win_rate | 0.4447 |
| sharpe_ratio | -8.8881 |
| sortino_ratio | -3.9579 |
| max_drawdown | 0.9933 |
| cagr | -0.8621 |
| net_avg_win | 26.4870 |
| net_avg_loss | -37.4618 |
| avg_hold_time_bars | 2.9205 |
| exposure | 0.1320 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
