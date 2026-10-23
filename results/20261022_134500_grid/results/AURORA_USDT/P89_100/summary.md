# EMA Hourly Continuation — AURORA/USDT P89_100

**Symbol:** AURORA/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 476 |
| net_profit_factor | 0.2420 |
| net_win_rate | 0.3466 |
| gross_profit_factor | 0.7916 |
| gross_win_rate | 0.4034 |
| sharpe_ratio | -9.3636 |
| sortino_ratio | -3.0005 |
| max_drawdown | 0.9837 |
| cagr | -0.8059 |
| net_avg_win | 19.0295 |
| net_avg_loss | -41.7265 |
| avg_hold_time_bars | 2.4034 |
| exposure | 0.0520 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
