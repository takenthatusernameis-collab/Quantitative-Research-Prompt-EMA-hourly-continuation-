# EMA Hourly Continuation — PEPE/USDT P34_55

**Symbol:** PEPE/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 889 |
| net_profit_factor | 0.4467 |
| net_win_rate | 0.4398 |
| gross_profit_factor | 0.8232 |
| gross_win_rate | 0.4511 |
| sharpe_ratio | -8.0932 |
| sortino_ratio | -3.4085 |
| max_drawdown | 0.9863 |
| cagr | -0.8186 |
| net_avg_win | 20.3614 |
| net_avg_loss | -35.7908 |
| avg_hold_time_bars | 2.6659 |
| exposure | 0.1077 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
