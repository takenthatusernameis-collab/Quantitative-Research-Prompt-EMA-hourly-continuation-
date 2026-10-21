# EMA Hourly Continuation — STRAX/USDT P8_21

**Symbol:** STRAX/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 750 |
| net_profit_factor | 0.4877 |
| net_win_rate | 0.4240 |
| gross_profit_factor | 0.7316 |
| gross_win_rate | 0.4240 |
| sharpe_ratio | -6.2972 |
| sortino_ratio | -2.4674 |
| max_drawdown | 0.9452 |
| cagr | -0.6831 |
| net_avg_win | 28.2389 |
| net_avg_loss | -42.6213 |
| avg_hold_time_bars | 6.3427 |
| exposure | 0.2175 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
