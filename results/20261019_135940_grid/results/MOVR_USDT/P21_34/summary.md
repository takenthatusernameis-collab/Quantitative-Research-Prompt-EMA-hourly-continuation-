# EMA Hourly Continuation — MOVR/USDT P21_34

**Symbol:** MOVR/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1177 |
| net_profit_factor | 0.3070 |
| net_win_rate | 0.4078 |
| gross_profit_factor | 0.7296 |
| gross_win_rate | 0.4410 |
| sharpe_ratio | -10.6225 |
| sortino_ratio | -5.1696 |
| max_drawdown | 0.9986 |
| cagr | -0.9262 |
| net_avg_win | 9.2139 |
| net_avg_loss | -20.6719 |
| avg_hold_time_bars | 2.7732 |
| exposure | 0.1484 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
