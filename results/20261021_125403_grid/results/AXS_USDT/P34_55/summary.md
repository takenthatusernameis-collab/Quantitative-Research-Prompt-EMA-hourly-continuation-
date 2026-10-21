# EMA Hourly Continuation — AXS/USDT P34_55

**Symbol:** AXS/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 307 |
| net_profit_factor | 0.6929 |
| net_win_rate | 0.4984 |
| gross_profit_factor | 0.9859 |
| gross_win_rate | 0.5016 |
| sharpe_ratio | -1.9203 |
| sortino_ratio | -0.4821 |
| max_drawdown | 0.4483 |
| cagr | -0.1973 |
| net_avg_win | 62.7596 |
| net_avg_loss | -89.9850 |
| avg_hold_time_bars | 5.6678 |
| exposure | 0.0787 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
