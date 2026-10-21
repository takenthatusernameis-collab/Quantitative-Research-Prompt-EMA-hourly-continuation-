# EMA Hourly Continuation — REZ/USDT P20_55

**Symbol:** REZ/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 549 |
| net_profit_factor | 0.8080 |
| net_win_rate | 0.4973 |
| gross_profit_factor | 1.0117 |
| gross_win_rate | 0.4973 |
| sharpe_ratio | -1.8386 |
| sortino_ratio | -0.6213 |
| max_drawdown | 0.6224 |
| cagr | -0.2491 |
| net_avg_win | 78.2879 |
| net_avg_loss | -95.8324 |
| avg_hold_time_bars | 8.8616 |
| exposure | 0.2245 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
