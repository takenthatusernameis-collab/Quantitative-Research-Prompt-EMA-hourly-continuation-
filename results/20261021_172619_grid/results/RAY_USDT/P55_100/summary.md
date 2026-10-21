# EMA Hourly Continuation — RAY/USDT P55_100

**Symbol:** RAY/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 330 |
| net_profit_factor | 0.8416 |
| net_win_rate | 0.5273 |
| gross_profit_factor | 1.0881 |
| gross_win_rate | 0.5273 |
| sharpe_ratio | -0.8724 |
| sortino_ratio | -0.2285 |
| max_drawdown | 0.3223 |
| cagr | -0.1011 |
| net_avg_win | 71.7108 |
| net_avg_loss | -95.0433 |
| avg_hold_time_bars | 7.8758 |
| exposure | 0.1181 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
