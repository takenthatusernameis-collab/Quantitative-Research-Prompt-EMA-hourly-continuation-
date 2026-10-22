# EMA Hourly Continuation — VR/USDT P21_144

**Symbol:** VR/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 335 |
| net_profit_factor | 0.6256 |
| net_win_rate | 0.4299 |
| gross_profit_factor | 0.7375 |
| gross_win_rate | 0.4299 |
| sharpe_ratio | -2.6198 |
| sortino_ratio | -0.6751 |
| max_drawdown | 0.5465 |
| cagr | -0.2701 |
| net_avg_win | 63.4219 |
| net_avg_loss | -76.4295 |
| avg_hold_time_bars | 30.2567 |
| exposure | 0.4607 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
