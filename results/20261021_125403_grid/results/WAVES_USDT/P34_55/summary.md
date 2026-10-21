# EMA Hourly Continuation — WAVES/USDT P34_55

**Symbol:** WAVES/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 339 |
| net_profit_factor | 0.4880 |
| net_win_rate | 0.4218 |
| gross_profit_factor | 0.7436 |
| gross_win_rate | 0.4218 |
| sharpe_ratio | -4.2513 |
| sortino_ratio | -1.1202 |
| max_drawdown | 0.7331 |
| cagr | -0.4055 |
| net_avg_win | 48.5903 |
| net_avg_loss | -72.6467 |
| avg_hold_time_bars | 5.9764 |
| exposure | 0.0921 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
