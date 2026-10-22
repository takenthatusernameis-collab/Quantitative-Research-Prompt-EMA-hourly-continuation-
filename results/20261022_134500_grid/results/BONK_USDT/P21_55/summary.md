# EMA Hourly Continuation — BONK/USDT P21_55

**Symbol:** BONK/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 942 |
| net_profit_factor | 0.5027 |
| net_win_rate | 0.4586 |
| gross_profit_factor | 0.8398 |
| gross_win_rate | 0.4724 |
| sharpe_ratio | -6.1956 |
| sortino_ratio | -2.6451 |
| max_drawdown | 0.9661 |
| cagr | -0.7344 |
| net_avg_win | 22.5649 |
| net_avg_loss | -38.0191 |
| avg_hold_time_bars | 5.3291 |
| exposure | 0.2282 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
