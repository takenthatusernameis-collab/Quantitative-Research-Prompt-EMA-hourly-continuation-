# EMA Hourly Continuation — XPR/USDT P8_26

**Symbol:** XPR/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1479 |
| net_profit_factor | 0.3195 |
| net_win_rate | 0.3834 |
| gross_profit_factor | 0.6744 |
| gross_win_rate | 0.4023 |
| sharpe_ratio | -14.0618 |
| sortino_ratio | -7.6549 |
| max_drawdown | 1.0000 |
| cagr | -0.9827 |
| net_avg_win | 8.2796 |
| net_avg_loss | -16.1120 |
| avg_hold_time_bars | 3.7485 |
| exposure | 0.2520 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
