# EMA Hourly Continuation — G/USDT P55_100

**Symbol:** G/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 484 |
| net_profit_factor | 0.4877 |
| net_win_rate | 0.4525 |
| gross_profit_factor | 0.8777 |
| gross_win_rate | 0.4711 |
| sharpe_ratio | -5.0765 |
| sortino_ratio | -1.7039 |
| max_drawdown | 0.8339 |
| cagr | -0.5564 |
| net_avg_win | 36.0246 |
| net_avg_loss | -61.0434 |
| avg_hold_time_bars | 6.6260 |
| exposure | 0.1686 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
