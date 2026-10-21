# EMA Hourly Continuation — UQC/USDT P8_50

**Symbol:** UQC/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 293 |
| net_profit_factor | 0.4308 |
| net_win_rate | 0.3447 |
| gross_profit_factor | 0.5956 |
| gross_win_rate | 0.3447 |
| sharpe_ratio | -4.9093 |
| sortino_ratio | -1.1655 |
| max_drawdown | 0.7615 |
| cagr | -0.4297 |
| net_avg_win | 56.7508 |
| net_avg_loss | -69.3021 |
| avg_hold_time_bars | 50.1536 |
| exposure | 0.6651 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
