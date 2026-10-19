# EMA Hourly Continuation — TWT/USDT P20_50

**Symbol:** TWT/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1055 |
| net_profit_factor | 0.3616 |
| net_win_rate | 0.4436 |
| gross_profit_factor | 0.7876 |
| gross_win_rate | 0.4711 |
| sharpe_ratio | -8.6595 |
| sortino_ratio | -3.9564 |
| max_drawdown | 0.9939 |
| cagr | -0.8653 |
| net_avg_win | 12.0231 |
| net_avg_loss | -26.5106 |
| avg_hold_time_bars | 4.6796 |
| exposure | 0.2244 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
