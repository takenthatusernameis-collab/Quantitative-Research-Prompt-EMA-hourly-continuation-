# EMA Hourly Continuation — TURBO/USDT P20_34

**Symbol:** TURBO/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1004 |
| net_profit_factor | 0.5228 |
| net_win_rate | 0.4382 |
| gross_profit_factor | 0.9028 |
| gross_win_rate | 0.4582 |
| sharpe_ratio | -9.1626 |
| sortino_ratio | -4.4733 |
| max_drawdown | 0.9911 |
| cagr | -0.8926 |
| net_avg_win | 24.6668 |
| net_avg_loss | -36.8078 |
| avg_hold_time_bars | 2.6504 |
| exposure | 0.1452 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
