# EMA Hourly Continuation — DOGS/USDT P89_100

**Symbol:** DOGS/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 535 |
| net_profit_factor | 0.2921 |
| net_win_rate | 0.4075 |
| gross_profit_factor | 0.6812 |
| gross_win_rate | 0.4224 |
| sharpe_ratio | -8.7088 |
| sortino_ratio | -3.0873 |
| max_drawdown | 0.9729 |
| cagr | -0.8101 |
| net_avg_win | 18.3999 |
| net_avg_loss | -43.3147 |
| avg_hold_time_bars | 1.9477 |
| exposure | 0.0553 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
