# EMA Hourly Continuation — LPT/USDT P20_34

**Symbol:** LPT/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1235 |
| net_profit_factor | 0.4128 |
| net_win_rate | 0.3968 |
| gross_profit_factor | 0.7955 |
| gross_win_rate | 0.4283 |
| sharpe_ratio | -11.6055 |
| sortino_ratio | -5.8163 |
| max_drawdown | 0.9994 |
| cagr | -0.9468 |
| net_avg_win | 14.3350 |
| net_avg_loss | -22.8427 |
| avg_hold_time_bars | 2.7474 |
| exposure | 0.1542 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
