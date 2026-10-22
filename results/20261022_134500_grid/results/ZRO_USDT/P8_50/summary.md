# EMA Hourly Continuation — ZRO/USDT P8_50

**Symbol:** ZRO/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1019 |
| net_profit_factor | 0.7130 |
| net_win_rate | 0.4975 |
| gross_profit_factor | 1.0764 |
| gross_win_rate | 0.5005 |
| sharpe_ratio | -4.2566 |
| sortino_ratio | -1.9726 |
| max_drawdown | 0.9016 |
| cagr | -0.6167 |
| net_avg_win | 43.7704 |
| net_avg_loss | -60.7879 |
| avg_hold_time_bars | 9.1992 |
| exposure | 0.4588 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
