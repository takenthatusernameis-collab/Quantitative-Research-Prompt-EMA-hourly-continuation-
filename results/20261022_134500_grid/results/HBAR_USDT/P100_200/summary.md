# EMA Hourly Continuation — HBAR/USDT P100_200

**Symbol:** HBAR/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 390 |
| net_profit_factor | 0.6262 |
| net_win_rate | 0.4923 |
| gross_profit_factor | 1.0202 |
| gross_win_rate | 0.4974 |
| sharpe_ratio | -3.2424 |
| sortino_ratio | -0.9038 |
| max_drawdown | 0.6951 |
| cagr | -0.3527 |
| net_avg_win | 57.9877 |
| net_avg_loss | -89.7954 |
| avg_hold_time_bars | 9.3897 |
| exposure | 0.1665 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
