# EMA Hourly Continuation — ZBCN/USDT P21_26

**Symbol:** ZBCN/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 112 |
| net_profit_factor | 0.8787 |
| net_win_rate | 0.5268 |
| gross_profit_factor | 1.1096 |
| gross_win_rate | 0.5268 |
| sharpe_ratio | -0.4220 |
| sortino_ratio | -0.0650 |
| max_drawdown | 0.1368 |
| cagr | -0.0303 |
| net_avg_win | 89.7023 |
| net_avg_loss | -113.6445 |
| avg_hold_time_bars | 5.5804 |
| exposure | 0.0289 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
