# EMA Hourly Continuation — TURBO/USDT P8_34

**Symbol:** TURBO/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1146 |
| net_profit_factor | 0.6006 |
| net_win_rate | 0.4572 |
| gross_profit_factor | 0.8942 |
| gross_win_rate | 0.4712 |
| sharpe_ratio | -7.2209 |
| sortino_ratio | -3.7725 |
| max_drawdown | 0.9787 |
| cagr | -0.8368 |
| net_avg_win | 28.0484 |
| net_avg_loss | -39.3442 |
| avg_hold_time_bars | 5.5218 |
| exposure | 0.3452 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
