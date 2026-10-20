# EMA Hourly Continuation — ALT/USDT P50_144

**Symbol:** ALT/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 453 |
| net_profit_factor | 0.6222 |
| net_win_rate | 0.4636 |
| gross_profit_factor | 0.8751 |
| gross_win_rate | 0.4746 |
| sharpe_ratio | -3.0430 |
| sortino_ratio | -0.9167 |
| max_drawdown | 0.6676 |
| cagr | -0.3478 |
| net_avg_win | 51.6021 |
| net_avg_loss | -71.6771 |
| avg_hold_time_bars | 15.2406 |
| exposure | 0.3138 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
