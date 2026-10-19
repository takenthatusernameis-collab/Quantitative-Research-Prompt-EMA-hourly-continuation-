# EMA Hourly Continuation — RAY/USDT P34_50

**Symbol:** RAY/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 860 |
| net_profit_factor | 0.4387 |
| net_win_rate | 0.4453 |
| gross_profit_factor | 0.8293 |
| gross_win_rate | 0.4581 |
| sharpe_ratio | -7.7719 |
| sortino_ratio | -3.2124 |
| max_drawdown | 0.9844 |
| cagr | -0.8009 |
| net_avg_win | 20.0558 |
| net_avg_loss | -36.7038 |
| avg_hold_time_bars | 2.9023 |
| exposure | 0.1135 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
