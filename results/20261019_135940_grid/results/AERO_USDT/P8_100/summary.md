# EMA Hourly Continuation — AERO/USDT P8_100

**Symbol:** AERO/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 589 |
| net_profit_factor | 0.8358 |
| net_win_rate | 0.5195 |
| gross_profit_factor | 1.0952 |
| gross_win_rate | 0.5229 |
| sharpe_ratio | -1.4035 |
| sortino_ratio | -0.4837 |
| max_drawdown | 0.4706 |
| cagr | -0.2069 |
| net_avg_win | 73.4311 |
| net_avg_loss | -94.9955 |
| avg_hold_time_bars | 25.0713 |
| exposure | 0.6712 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
