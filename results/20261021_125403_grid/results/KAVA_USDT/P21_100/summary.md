# EMA Hourly Continuation — KAVA/USDT P21_100

**Symbol:** KAVA/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 490 |
| net_profit_factor | 0.7127 |
| net_win_rate | 0.4878 |
| gross_profit_factor | 0.9710 |
| gross_win_rate | 0.4878 |
| sharpe_ratio | -2.5923 |
| sortino_ratio | -0.8192 |
| max_drawdown | 0.6324 |
| cagr | -0.3145 |
| net_avg_win | 63.5963 |
| net_avg_loss | -84.9629 |
| avg_hold_time_bars | 19.6755 |
| exposure | 0.4382 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
