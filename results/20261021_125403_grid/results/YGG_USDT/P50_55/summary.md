# EMA Hourly Continuation — YGG/USDT P50_55

**Symbol:** YGG/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 147 |
| net_profit_factor | 0.8152 |
| net_win_rate | 0.5510 |
| gross_profit_factor | 1.2153 |
| gross_win_rate | 0.5510 |
| sharpe_ratio | -0.7426 |
| sortino_ratio | -0.1303 |
| max_drawdown | 0.1891 |
| cagr | -0.0581 |
| net_avg_win | 76.3181 |
| net_avg_loss | -114.8893 |
| avg_hold_time_bars | 4.1497 |
| exposure | 0.0276 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
