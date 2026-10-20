# EMA Hourly Continuation — CATI/USDT P26_200

**Symbol:** CATI/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 354 |
| net_profit_factor | 0.4606 |
| net_win_rate | 0.4040 |
| gross_profit_factor | 0.7139 |
| gross_win_rate | 0.4322 |
| sharpe_ratio | -4.9203 |
| sortino_ratio | -1.4167 |
| max_drawdown | 0.7814 |
| cagr | -0.5027 |
| net_avg_win | 45.7782 |
| net_avg_loss | -67.3532 |
| avg_hold_time_bars | 31.8870 |
| exposure | 0.6188 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
