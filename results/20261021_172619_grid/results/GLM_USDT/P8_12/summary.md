# EMA Hourly Continuation — GLM/USDT P8_12

**Symbol:** GLM/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 504 |
| net_profit_factor | 0.6522 |
| net_win_rate | 0.5119 |
| gross_profit_factor | 1.0999 |
| gross_win_rate | 0.5139 |
| sharpe_ratio | -3.4514 |
| sortino_ratio | -1.1168 |
| max_drawdown | 0.7516 |
| cagr | -0.4009 |
| net_avg_win | 52.6107 |
| net_avg_loss | -84.5981 |
| avg_hold_time_bars | 4.6369 |
| exposure | 0.1062 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
