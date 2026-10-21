# EMA Hourly Continuation — LDO/USDT P8_34

**Symbol:** LDO/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 734 |
| net_profit_factor | 0.7015 |
| net_win_rate | 0.4741 |
| gross_profit_factor | 0.8850 |
| gross_win_rate | 0.4741 |
| sharpe_ratio | -2.9417 |
| sortino_ratio | -1.1362 |
| max_drawdown | 0.7378 |
| cagr | -0.4067 |
| net_avg_win | 49.3402 |
| net_avg_loss | -63.4067 |
| avg_hold_time_bars | 8.7548 |
| exposure | 0.2921 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
