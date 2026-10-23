# EMA Hourly Continuation — MERL/USDT P20_21

**Symbol:** MERL/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1233 |
| net_profit_factor | 0.2097 |
| net_win_rate | 0.3228 |
| gross_profit_factor | 0.5195 |
| gross_win_rate | 0.3852 |
| sharpe_ratio | -15.3187 |
| sortino_ratio | -7.8002 |
| max_drawdown | 1.0000 |
| cagr | -0.9856 |
| net_avg_win | 6.6678 |
| net_avg_loss | -15.1540 |
| avg_hold_time_bars | 1.8005 |
| exposure | 0.1012 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
