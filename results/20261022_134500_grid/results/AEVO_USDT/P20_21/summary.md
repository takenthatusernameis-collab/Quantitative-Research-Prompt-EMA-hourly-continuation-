# EMA Hourly Continuation — AEVO/USDT P20_21

**Symbol:** AEVO/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1239 |
| net_profit_factor | 0.1795 |
| net_win_rate | 0.3261 |
| gross_profit_factor | 0.6146 |
| gross_win_rate | 0.3931 |
| sharpe_ratio | -16.4450 |
| sortino_ratio | -8.5500 |
| max_drawdown | 1.0000 |
| cagr | -0.9910 |
| net_avg_win | 5.4136 |
| net_avg_loss | -14.5953 |
| avg_hold_time_bars | 1.9387 |
| exposure | 0.1087 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
