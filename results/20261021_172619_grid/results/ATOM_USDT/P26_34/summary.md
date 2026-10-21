# EMA Hourly Continuation — ATOM/USDT P26_34

**Symbol:** ATOM/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 144 |
| net_profit_factor | 0.6196 |
| net_win_rate | 0.4861 |
| gross_profit_factor | 0.9260 |
| gross_win_rate | 0.4861 |
| sharpe_ratio | -1.6895 |
| sortino_ratio | -0.2914 |
| max_drawdown | 0.2910 |
| cagr | -0.1247 |
| net_avg_win | 66.1579 |
| net_avg_loss | -101.0075 |
| avg_hold_time_bars | 5.5833 |
| exposure | 0.0365 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
