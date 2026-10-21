# EMA Hourly Continuation — DODO/USDT P8_55

**Symbol:** DODO/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 753 |
| net_profit_factor | 0.6911 |
| net_win_rate | 0.4595 |
| gross_profit_factor | 0.8627 |
| gross_win_rate | 0.4595 |
| sharpe_ratio | -3.3621 |
| sortino_ratio | -1.3076 |
| max_drawdown | 0.7869 |
| cagr | -0.4520 |
| net_avg_win | 50.4792 |
| net_avg_loss | -62.0959 |
| avg_hold_time_bars | 13.0850 |
| exposure | 0.4459 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
