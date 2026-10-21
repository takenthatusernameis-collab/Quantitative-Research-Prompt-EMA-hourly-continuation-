# EMA Hourly Continuation — LINK/USDT P12_26

**Symbol:** LINK/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 387 |
| net_profit_factor | 0.7439 |
| net_win_rate | 0.5065 |
| gross_profit_factor | 1.0472 |
| gross_win_rate | 0.5065 |
| sharpe_ratio | -2.0072 |
| sortino_ratio | -0.5680 |
| max_drawdown | 0.5579 |
| cagr | -0.2291 |
| net_avg_win | 71.0960 |
| net_avg_loss | -98.0729 |
| avg_hold_time_bars | 5.8527 |
| exposure | 0.1030 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
