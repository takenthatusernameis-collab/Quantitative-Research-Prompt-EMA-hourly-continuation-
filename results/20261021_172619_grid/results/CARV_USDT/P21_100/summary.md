# EMA Hourly Continuation — CARV/USDT P21_100

**Symbol:** CARV/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 367 |
| net_profit_factor | 0.7386 |
| net_win_rate | 0.4768 |
| gross_profit_factor | 0.9171 |
| gross_win_rate | 0.4768 |
| sharpe_ratio | -2.0870 |
| sortino_ratio | -0.6338 |
| max_drawdown | 0.4783 |
| cagr | -0.2536 |
| net_avg_win | 72.2547 |
| net_avg_loss | -89.1656 |
| avg_hold_time_bars | 19.7248 |
| exposure | 0.4074 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
