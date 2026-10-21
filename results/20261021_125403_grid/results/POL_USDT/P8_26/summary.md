# EMA Hourly Continuation — POL/USDT P8_26

**Symbol:** POL/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 611 |
| net_profit_factor | 0.6515 |
| net_win_rate | 0.4812 |
| gross_profit_factor | 0.9120 |
| gross_win_rate | 0.4812 |
| sharpe_ratio | -3.1817 |
| sortino_ratio | -1.1265 |
| max_drawdown | 0.7581 |
| cagr | -0.4022 |
| net_avg_win | 46.1114 |
| net_avg_loss | -65.6445 |
| avg_hold_time_bars | 6.8298 |
| exposure | 0.1897 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
