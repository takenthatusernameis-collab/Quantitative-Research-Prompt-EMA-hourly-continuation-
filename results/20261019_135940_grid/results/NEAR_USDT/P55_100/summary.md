# EMA Hourly Continuation — NEAR/USDT P55_100

**Symbol:** NEAR/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 606 |
| net_profit_factor | 0.5260 |
| net_win_rate | 0.4620 |
| gross_profit_factor | 0.8911 |
| gross_win_rate | 0.4686 |
| sharpe_ratio | -4.9094 |
| sortino_ratio | -1.6971 |
| max_drawdown | 0.8780 |
| cagr | -0.5649 |
| net_avg_win | 34.7301 |
| net_avg_loss | -56.7092 |
| avg_hold_time_bars | 4.2954 |
| exposure | 0.1183 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
