# EMA Hourly Continuation — SUPER/USDT P50_100

**Symbol:** SUPER/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 359 |
| net_profit_factor | 0.7962 |
| net_win_rate | 0.5181 |
| gross_profit_factor | 1.0458 |
| gross_win_rate | 0.5181 |
| sharpe_ratio | -1.2204 |
| sortino_ratio | -0.3328 |
| max_drawdown | 0.3505 |
| cagr | -0.1420 |
| net_avg_win | 67.0449 |
| net_avg_loss | -90.5346 |
| avg_hold_time_bars | 10.1811 |
| exposure | 0.1661 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
