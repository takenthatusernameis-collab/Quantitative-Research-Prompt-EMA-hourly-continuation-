# EMA Hourly Continuation — YGG/USDT P8_20

**Symbol:** YGG/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1695 |
| net_profit_factor | 0.4479 |
| net_win_rate | 0.4342 |
| gross_profit_factor | 0.8461 |
| gross_win_rate | 0.4525 |
| sharpe_ratio | -11.0140 |
| sortino_ratio | -6.4095 |
| max_drawdown | 0.9996 |
| cagr | -0.9564 |
| net_avg_win | 11.0178 |
| net_avg_loss | -18.8795 |
| avg_hold_time_bars | 2.9221 |
| exposure | 0.2241 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
