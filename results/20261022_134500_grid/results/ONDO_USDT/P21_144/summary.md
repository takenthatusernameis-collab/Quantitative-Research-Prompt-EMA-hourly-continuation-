# EMA Hourly Continuation — ONDO/USDT P21_144

**Symbol:** ONDO/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 541 |
| net_profit_factor | 0.7325 |
| net_win_rate | 0.4954 |
| gross_profit_factor | 1.0327 |
| gross_win_rate | 0.5028 |
| sharpe_ratio | -2.5770 |
| sortino_ratio | -0.8409 |
| max_drawdown | 0.6779 |
| cagr | -0.3315 |
| net_avg_win | 65.0213 |
| net_avg_loss | -87.1355 |
| avg_hold_time_bars | 19.2181 |
| exposure | 0.4726 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
