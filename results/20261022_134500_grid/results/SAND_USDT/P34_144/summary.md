# EMA Hourly Continuation — SAND/USDT P34_144

**Symbol:** SAND/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 478 |
| net_profit_factor | 0.5685 |
| net_win_rate | 0.4644 |
| gross_profit_factor | 0.8908 |
| gross_win_rate | 0.4728 |
| sharpe_ratio | -3.8500 |
| sortino_ratio | -1.1861 |
| max_drawdown | 0.7662 |
| cagr | -0.4322 |
| net_avg_win | 45.0243 |
| net_avg_loss | -68.6765 |
| avg_hold_time_bars | 17.8808 |
| exposure | 0.3885 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
