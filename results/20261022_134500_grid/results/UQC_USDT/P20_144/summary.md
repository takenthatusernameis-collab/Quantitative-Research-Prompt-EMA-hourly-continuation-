# EMA Hourly Continuation — UQC/USDT P20_144

**Symbol:** UQC/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 232 |
| net_profit_factor | 0.3304 |
| net_win_rate | 0.3103 |
| gross_profit_factor | 0.4477 |
| gross_win_rate | 0.3103 |
| sharpe_ratio | -4.9677 |
| sortino_ratio | -1.0502 |
| max_drawdown | 0.7274 |
| cagr | -0.4027 |
| net_avg_win | 49.8542 |
| net_avg_loss | -67.8955 |
| avg_hold_time_bars | 66.4526 |
| exposure | 0.6978 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
