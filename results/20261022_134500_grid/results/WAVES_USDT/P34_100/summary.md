# EMA Hourly Continuation — WAVES/USDT P34_100

**Symbol:** WAVES/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 763 |
| net_profit_factor | 0.4648 |
| net_win_rate | 0.4273 |
| gross_profit_factor | 0.8525 |
| gross_win_rate | 0.4443 |
| sharpe_ratio | -7.0355 |
| sortino_ratio | -2.7338 |
| max_drawdown | 0.9676 |
| cagr | -0.7423 |
| net_avg_win | 25.7581 |
| net_avg_loss | -41.3391 |
| avg_hold_time_bars | 8.1547 |
| exposure | 0.2828 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
