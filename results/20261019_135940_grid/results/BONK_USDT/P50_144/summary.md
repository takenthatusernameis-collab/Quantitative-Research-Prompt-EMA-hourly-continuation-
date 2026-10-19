# EMA Hourly Continuation — BONK/USDT P50_144

**Symbol:** BONK/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 457 |
| net_profit_factor | 0.6759 |
| net_win_rate | 0.4880 |
| gross_profit_factor | 0.9431 |
| gross_win_rate | 0.4902 |
| sharpe_ratio | -2.6032 |
| sortino_ratio | -0.7892 |
| max_drawdown | 0.6271 |
| cagr | -0.3089 |
| net_avg_win | 56.5322 |
| net_avg_loss | -79.7094 |
| avg_hold_time_bars | 13.8140 |
| exposure | 0.2870 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
