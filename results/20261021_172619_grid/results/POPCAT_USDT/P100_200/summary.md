# EMA Hourly Continuation — POPCAT/USDT P100_200

**Symbol:** POPCAT/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 238 |
| net_profit_factor | 0.8076 |
| net_win_rate | 0.4958 |
| gross_profit_factor | 0.9765 |
| gross_win_rate | 0.4958 |
| sharpe_ratio | -1.1059 |
| sortino_ratio | -0.2629 |
| max_drawdown | 0.2518 |
| cagr | -0.1150 |
| net_avg_win | 82.5313 |
| net_avg_loss | -100.4942 |
| avg_hold_time_bars | 14.0882 |
| exposure | 0.1771 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
