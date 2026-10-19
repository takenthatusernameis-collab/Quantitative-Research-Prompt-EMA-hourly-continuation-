# EMA Hourly Continuation — NEO/USDT P8_12

**Symbol:** NEO/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1849 |
| net_profit_factor | 0.1832 |
| net_win_rate | 0.3494 |
| gross_profit_factor | 0.7613 |
| gross_win_rate | 0.4343 |
| sharpe_ratio | -19.0375 |
| sortino_ratio | -11.9918 |
| max_drawdown | 1.0000 |
| cagr | -0.9984 |
| net_avg_win | 3.4729 |
| net_avg_loss | -10.1775 |
| avg_hold_time_bars | 1.9113 |
| exposure | 0.1606 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
