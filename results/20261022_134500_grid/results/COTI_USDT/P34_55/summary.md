# EMA Hourly Continuation — COTI/USDT P34_55

**Symbol:** COTI/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 920 |
| net_profit_factor | 0.4541 |
| net_win_rate | 0.4391 |
| gross_profit_factor | 0.8456 |
| gross_win_rate | 0.4478 |
| sharpe_ratio | -7.8552 |
| sortino_ratio | -3.3813 |
| max_drawdown | 0.9845 |
| cagr | -0.8083 |
| net_avg_win | 20.2610 |
| net_avg_loss | -34.9371 |
| avg_hold_time_bars | 3.0652 |
| exposure | 0.1282 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
