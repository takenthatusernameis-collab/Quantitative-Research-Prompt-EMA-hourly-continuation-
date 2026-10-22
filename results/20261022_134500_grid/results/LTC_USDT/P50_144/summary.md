# EMA Hourly Continuation — LTC/USDT P50_144

**Symbol:** LTC/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 543 |
| net_profit_factor | 0.3250 |
| net_win_rate | 0.4070 |
| gross_profit_factor | 0.7202 |
| gross_win_rate | 0.4420 |
| sharpe_ratio | -6.6505 |
| sortino_ratio | -2.1897 |
| max_drawdown | 0.9379 |
| cagr | -0.6629 |
| net_avg_win | 20.3663 |
| net_avg_loss | -43.0102 |
| avg_hold_time_bars | 11.2873 |
| exposure | 0.2786 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
