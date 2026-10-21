# EMA Hourly Continuation — DASH/USDT P21_100

**Symbol:** DASH/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 433 |
| net_profit_factor | 0.7372 |
| net_win_rate | 0.4804 |
| gross_profit_factor | 0.9522 |
| gross_win_rate | 0.4804 |
| sharpe_ratio | -2.1179 |
| sortino_ratio | -0.6288 |
| max_drawdown | 0.5587 |
| cagr | -0.2505 |
| net_avg_win | 69.4971 |
| net_avg_loss | -87.1463 |
| avg_hold_time_bars | 20.0139 |
| exposure | 0.3939 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
