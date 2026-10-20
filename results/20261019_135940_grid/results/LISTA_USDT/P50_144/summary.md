# EMA Hourly Continuation — LISTA/USDT P50_144

**Symbol:** LISTA/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 426 |
| net_profit_factor | 0.6712 |
| net_win_rate | 0.4836 |
| gross_profit_factor | 0.9439 |
| gross_win_rate | 0.4859 |
| sharpe_ratio | -2.6826 |
| sortino_ratio | -0.8136 |
| max_drawdown | 0.5930 |
| cagr | -0.3164 |
| net_avg_win | 58.3249 |
| net_avg_loss | -81.3665 |
| avg_hold_time_bars | 15.5728 |
| exposure | 0.3244 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
