# EMA Hourly Continuation — STRAX/USDT P34_100

**Symbol:** STRAX/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 720 |
| net_profit_factor | 0.4901 |
| net_win_rate | 0.4153 |
| gross_profit_factor | 0.8066 |
| gross_win_rate | 0.4333 |
| sharpe_ratio | -6.9390 |
| sortino_ratio | -2.6294 |
| max_drawdown | 0.9607 |
| cagr | -0.7243 |
| net_avg_win | 30.8569 |
| net_avg_loss | -44.7161 |
| avg_hold_time_bars | 8.7556 |
| exposure | 0.2882 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
