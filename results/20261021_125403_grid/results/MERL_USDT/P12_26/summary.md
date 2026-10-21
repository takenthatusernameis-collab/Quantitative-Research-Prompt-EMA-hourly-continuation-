# EMA Hourly Continuation — MERL/USDT P12_26

**Symbol:** MERL/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 533 |
| net_profit_factor | 0.7539 |
| net_win_rate | 0.4897 |
| gross_profit_factor | 0.9605 |
| gross_win_rate | 0.4897 |
| sharpe_ratio | -2.0843 |
| sortino_ratio | -0.6890 |
| max_drawdown | 0.5525 |
| cagr | -0.2720 |
| net_avg_win | 64.3666 |
| net_avg_loss | -81.9237 |
| avg_hold_time_bars | 5.6642 |
| exposure | 0.1376 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
