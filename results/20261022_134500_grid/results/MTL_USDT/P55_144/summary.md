# EMA Hourly Continuation — MTL/USDT P55_144

**Symbol:** MTL/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 445 |
| net_profit_factor | 0.4758 |
| net_win_rate | 0.4360 |
| gross_profit_factor | 0.8177 |
| gross_win_rate | 0.4562 |
| sharpe_ratio | -4.7789 |
| sortino_ratio | -1.4145 |
| max_drawdown | 0.8246 |
| cagr | -0.4970 |
| net_avg_win | 38.5245 |
| net_avg_loss | -62.5786 |
| avg_hold_time_bars | 14.6966 |
| exposure | 0.2960 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
