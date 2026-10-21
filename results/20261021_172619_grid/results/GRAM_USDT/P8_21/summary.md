# EMA Hourly Continuation — GRAM/USDT P8_21

**Symbol:** GRAM/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 410 |
| net_profit_factor | 0.6992 |
| net_win_rate | 0.5098 |
| gross_profit_factor | 1.0416 |
| gross_win_rate | 0.5098 |
| sharpe_ratio | -2.2419 |
| sortino_ratio | -0.6540 |
| max_drawdown | 0.5567 |
| cagr | -0.2576 |
| net_avg_win | 58.5706 |
| net_avg_loss | -87.1080 |
| avg_hold_time_bars | 6.0195 |
| exposure | 0.1122 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
