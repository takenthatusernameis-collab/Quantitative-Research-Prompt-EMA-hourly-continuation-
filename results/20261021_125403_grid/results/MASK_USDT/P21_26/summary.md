# EMA Hourly Continuation — MASK/USDT P21_26

**Symbol:** MASK/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 271 |
| net_profit_factor | 0.6457 |
| net_win_rate | 0.5166 |
| gross_profit_factor | 1.1049 |
| gross_win_rate | 0.5240 |
| sharpe_ratio | -2.2028 |
| sortino_ratio | -0.5201 |
| max_drawdown | 0.4772 |
| cagr | -0.2135 |
| net_avg_win | 58.9488 |
| net_avg_loss | -97.5647 |
| avg_hold_time_bars | 6.1919 |
| exposure | 0.0763 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
