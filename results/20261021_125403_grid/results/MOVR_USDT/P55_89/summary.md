# EMA Hourly Continuation — MOVR/USDT P55_89

**Symbol:** MOVR/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 345 |
| net_profit_factor | 0.5720 |
| net_win_rate | 0.4377 |
| gross_profit_factor | 0.7757 |
| gross_win_rate | 0.4377 |
| sharpe_ratio | -3.2191 |
| sortino_ratio | -0.8503 |
| max_drawdown | 0.6492 |
| cagr | -0.3240 |
| net_avg_win | 55.4020 |
| net_avg_loss | -75.3848 |
| avg_hold_time_bars | 6.6899 |
| exposure | 0.1049 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
