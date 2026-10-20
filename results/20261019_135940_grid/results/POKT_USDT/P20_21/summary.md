# EMA Hourly Continuation — POKT/USDT P20_21

**Symbol:** POKT/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1275 |
| net_profit_factor | 0.2173 |
| net_win_rate | 0.2533 |
| gross_profit_factor | 0.8671 |
| gross_win_rate | 0.3349 |
| sharpe_ratio | -18.2802 |
| sortino_ratio | -9.6429 |
| max_drawdown | 1.0000 |
| cagr | -0.9948 |
| net_avg_win | 8.5951 |
| net_avg_loss | -13.4204 |
| avg_hold_time_bars | 2.6275 |
| exposure | 0.1516 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
