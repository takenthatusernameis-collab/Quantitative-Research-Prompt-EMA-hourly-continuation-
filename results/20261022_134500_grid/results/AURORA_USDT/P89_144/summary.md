# EMA Hourly Continuation — AURORA/USDT P89_144

**Symbol:** AURORA/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 403 |
| net_profit_factor | 0.4841 |
| net_win_rate | 0.4541 |
| gross_profit_factor | 0.9158 |
| gross_win_rate | 0.4615 |
| sharpe_ratio | -4.6946 |
| sortino_ratio | -1.3304 |
| max_drawdown | 0.8109 |
| cagr | -0.4811 |
| net_avg_win | 41.3946 |
| net_avg_loss | -71.1344 |
| avg_hold_time_bars | 5.6005 |
| exposure | 0.1026 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
