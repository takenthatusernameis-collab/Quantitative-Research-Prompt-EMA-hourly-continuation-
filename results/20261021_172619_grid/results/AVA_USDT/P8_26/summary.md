# EMA Hourly Continuation — AVA/USDT P8_26

**Symbol:** AVA/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 682 |
| net_profit_factor | 0.6951 |
| net_win_rate | 0.4912 |
| gross_profit_factor | 0.9620 |
| gross_win_rate | 0.4912 |
| sharpe_ratio | -3.0604 |
| sortino_ratio | -1.1462 |
| max_drawdown | 0.7488 |
| cagr | -0.4072 |
| net_avg_win | 49.7405 |
| net_avg_loss | -69.0888 |
| avg_hold_time_bars | 6.1496 |
| exposure | 0.1906 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
