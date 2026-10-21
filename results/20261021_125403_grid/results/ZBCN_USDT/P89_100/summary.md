# EMA Hourly Continuation — ZBCN/USDT P89_100

**Symbol:** ZBCN/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 84 |
| net_profit_factor | 0.7626 |
| net_win_rate | 0.4881 |
| gross_profit_factor | 0.9495 |
| gross_win_rate | 0.4881 |
| sharpe_ratio | -0.7710 |
| sortino_ratio | -0.1019 |
| max_drawdown | 0.1416 |
| cagr | -0.0458 |
| net_avg_win | 85.5494 |
| net_avg_loss | -106.9695 |
| avg_hold_time_bars | 5.0357 |
| exposure | 0.0196 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
