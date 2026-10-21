# EMA Hourly Continuation — ZRO/USDT P20_34

**Symbol:** ZRO/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 287 |
| net_profit_factor | 0.7693 |
| net_win_rate | 0.4948 |
| gross_profit_factor | 0.9952 |
| gross_win_rate | 0.4948 |
| sharpe_ratio | -1.5465 |
| sortino_ratio | -0.3896 |
| max_drawdown | 0.4270 |
| cagr | -0.1641 |
| net_avg_win | 80.2133 |
| net_avg_loss | -102.1164 |
| avg_hold_time_bars | 5.2927 |
| exposure | 0.0743 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
