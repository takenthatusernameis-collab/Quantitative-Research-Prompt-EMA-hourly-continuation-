# EMA Hourly Continuation — AURORA/USDT P8_100

**Symbol:** AURORA/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 480 |
| net_profit_factor | 0.7998 |
| net_win_rate | 0.4917 |
| gross_profit_factor | 0.9934 |
| gross_win_rate | 0.4917 |
| sharpe_ratio | -1.7461 |
| sortino_ratio | -0.5460 |
| max_drawdown | 0.5517 |
| cagr | -0.2233 |
| net_avg_win | 79.5421 |
| net_avg_loss | -96.1893 |
| avg_hold_time_bars | 28.6938 |
| exposure | 0.6260 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
