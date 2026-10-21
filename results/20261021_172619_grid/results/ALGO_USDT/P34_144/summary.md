# EMA Hourly Continuation — ALGO/USDT P34_144

**Symbol:** ALGO/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 377 |
| net_profit_factor | 0.7993 |
| net_win_rate | 0.5013 |
| gross_profit_factor | 1.0021 |
| gross_win_rate | 0.5013 |
| sharpe_ratio | -1.3675 |
| sortino_ratio | -0.3801 |
| max_drawdown | 0.3703 |
| cagr | -0.1607 |
| net_avg_win | 74.9879 |
| net_avg_loss | -94.3188 |
| avg_hold_time_bars | 20.1857 |
| exposure | 0.3459 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
