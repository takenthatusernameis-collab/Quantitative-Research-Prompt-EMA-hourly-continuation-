# EMA Hourly Continuation — AXS/USDT P8_50

**Symbol:** AXS/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 650 |
| net_profit_factor | 0.8643 |
| net_win_rate | 0.5292 |
| gross_profit_factor | 1.1171 |
| gross_win_rate | 0.5292 |
| sharpe_ratio | -1.1375 |
| sortino_ratio | -0.4176 |
| max_drawdown | 0.4216 |
| cagr | -0.1775 |
| net_avg_win | 72.0884 |
| net_avg_loss | -93.7592 |
| avg_hold_time_bars | 15.6077 |
| exposure | 0.4591 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
