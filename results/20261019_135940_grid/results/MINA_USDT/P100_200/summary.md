# EMA Hourly Continuation — MINA/USDT P100_200

**Symbol:** MINA/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 370 |
| net_profit_factor | 0.7262 |
| net_win_rate | 0.5189 |
| gross_profit_factor | 1.0714 |
| gross_win_rate | 0.5216 |
| sharpe_ratio | -1.8276 |
| sortino_ratio | -0.5043 |
| max_drawdown | 0.4651 |
| cagr | -0.2088 |
| net_avg_win | 61.4245 |
| net_avg_loss | -91.2341 |
| avg_hold_time_bars | 11.2784 |
| exposure | 0.1897 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
