# EMA Hourly Continuation — ZRO/USDT P21_55

**Symbol:** ZRO/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 912 |
| net_profit_factor | 0.6397 |
| net_win_rate | 0.4978 |
| gross_profit_factor | 1.0044 |
| gross_win_rate | 0.5011 |
| sharpe_ratio | -4.4232 |
| sortino_ratio | -1.9497 |
| max_drawdown | 0.8912 |
| cagr | -0.6086 |
| net_avg_win | 34.7212 |
| net_avg_loss | -53.8027 |
| avg_hold_time_bars | 5.1414 |
| exposure | 0.2295 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
