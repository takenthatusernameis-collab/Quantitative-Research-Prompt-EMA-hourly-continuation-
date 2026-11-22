# EMA Hourly Continuation — AZERO/USDT P26_50

**Symbol:** AZERO/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 824 |
| net_profit_factor | 0.4253 |
| net_win_rate | 0.4053 |
| gross_profit_factor | 0.8129 |
| gross_win_rate | 0.4248 |
| sharpe_ratio | -7.7788 |
| sortino_ratio | -3.1311 |
| max_drawdown | 0.9805 |
| cagr | -0.7881 |
| net_avg_win | 21.7159 |
| net_avg_loss | -34.8032 |
| avg_hold_time_bars | 5.0425 |
| exposure | 0.1880 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
