# EMA Hourly Continuation — CPOOL/USDT P34_50

**Symbol:** CPOOL/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 864 |
| net_profit_factor | 0.3883 |
| net_win_rate | 0.3981 |
| gross_profit_factor | 0.6635 |
| gross_win_rate | 0.4167 |
| sharpe_ratio | -9.0759 |
| sortino_ratio | -3.7290 |
| max_drawdown | 0.9927 |
| cagr | -0.8578 |
| net_avg_win | 18.3133 |
| net_avg_loss | -31.2022 |
| avg_hold_time_bars | 2.7905 |
| exposure | 0.1096 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
