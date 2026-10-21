# EMA Hourly Continuation — ALT/USDT P34_144

**Symbol:** ALT/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 381 |
| net_profit_factor | 0.7107 |
| net_win_rate | 0.4698 |
| gross_profit_factor | 0.8644 |
| gross_win_rate | 0.4698 |
| sharpe_ratio | -1.9915 |
| sortino_ratio | -0.5525 |
| max_drawdown | 0.4829 |
| cagr | -0.2255 |
| net_avg_win | 64.9894 |
| net_avg_loss | -81.0379 |
| avg_hold_time_bars | 24.0367 |
| exposure | 0.4163 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
