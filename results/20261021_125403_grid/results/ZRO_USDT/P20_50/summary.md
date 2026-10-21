# EMA Hourly Continuation — ZRO/USDT P20_50

**Symbol:** ZRO/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 477 |
| net_profit_factor | 0.7957 |
| net_win_rate | 0.4990 |
| gross_profit_factor | 0.9909 |
| gross_win_rate | 0.4990 |
| sharpe_ratio | -1.5995 |
| sortino_ratio | -0.5194 |
| max_drawdown | 0.4476 |
| cagr | -0.2133 |
| net_avg_win | 70.1360 |
| net_avg_loss | -87.7719 |
| avg_hold_time_bars | 7.5912 |
| exposure | 0.1772 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
