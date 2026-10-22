# EMA Hourly Continuation — LUNA/USDT P34_50

**Symbol:** LUNA/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 205 |
| net_profit_factor | 0.8583 |
| net_win_rate | 0.5463 |
| gross_profit_factor | 1.1932 |
| gross_win_rate | 0.5463 |
| sharpe_ratio | -0.6432 |
| sortino_ratio | -0.1337 |
| max_drawdown | 0.1928 |
| cagr | -0.0603 |
| net_avg_win | 78.2067 |
| net_avg_loss | -109.7369 |
| avg_hold_time_bars | 5.4293 |
| exposure | 0.0506 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
