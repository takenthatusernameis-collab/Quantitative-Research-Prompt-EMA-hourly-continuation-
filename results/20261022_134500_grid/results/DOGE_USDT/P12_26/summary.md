# EMA Hourly Continuation — DOGE/USDT P12_26

**Symbol:** DOGE/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1378 |
| net_profit_factor | 0.3330 |
| net_win_rate | 0.4209 |
| gross_profit_factor | 0.8461 |
| gross_win_rate | 0.4557 |
| sharpe_ratio | -12.0814 |
| sortino_ratio | -6.3175 |
| max_drawdown | 0.9998 |
| cagr | -0.9646 |
| net_avg_win | 8.6057 |
| net_avg_loss | -18.7833 |
| avg_hold_time_bars | 2.7003 |
| exposure | 0.1691 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
