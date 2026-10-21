# EMA Hourly Continuation — QI/USDT P8_26

**Symbol:** QI/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 813 |
| net_profit_factor | 0.6866 |
| net_win_rate | 0.4969 |
| gross_profit_factor | 0.9711 |
| gross_win_rate | 0.4969 |
| sharpe_ratio | -3.3273 |
| sortino_ratio | -1.3580 |
| max_drawdown | 0.7941 |
| cagr | -0.4616 |
| net_avg_win | 42.8461 |
| net_avg_loss | -61.6444 |
| avg_hold_time_bars | 6.7540 |
| exposure | 0.2485 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
