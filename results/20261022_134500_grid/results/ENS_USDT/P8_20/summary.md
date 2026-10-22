# EMA Hourly Continuation — ENS/USDT P8_20

**Symbol:** ENS/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1739 |
| net_profit_factor | 0.4317 |
| net_win_rate | 0.4175 |
| gross_profit_factor | 0.8883 |
| gross_win_rate | 0.4439 |
| sharpe_ratio | -12.8936 |
| sortino_ratio | -7.6157 |
| max_drawdown | 0.9999 |
| cagr | -0.9784 |
| net_avg_win | 10.4608 |
| net_avg_loss | -17.3681 |
| avg_hold_time_bars | 2.9523 |
| exposure | 0.2334 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
