# EMA Hourly Continuation — PENDLE/USDT P50_55

**Symbol:** PENDLE/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 116 |
| net_profit_factor | 0.7715 |
| net_win_rate | 0.5086 |
| gross_profit_factor | 1.0187 |
| gross_win_rate | 0.5086 |
| sharpe_ratio | -0.8256 |
| sortino_ratio | -0.1278 |
| max_drawdown | 0.1610 |
| cagr | -0.0574 |
| net_avg_win | 78.9558 |
| net_avg_loss | -105.9258 |
| avg_hold_time_bars | 5.9483 |
| exposure | 0.0314 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
