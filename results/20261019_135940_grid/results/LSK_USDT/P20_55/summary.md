# EMA Hourly Continuation — LSK/USDT P20_55

**Symbol:** LSK/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 814 |
| net_profit_factor | 0.5372 |
| net_win_rate | 0.4619 |
| gross_profit_factor | 0.9276 |
| gross_win_rate | 0.4742 |
| sharpe_ratio | -5.7068 |
| sortino_ratio | -2.3039 |
| max_drawdown | 0.9401 |
| cagr | -0.6662 |
| net_avg_win | 28.9085 |
| net_avg_loss | -46.1960 |
| avg_hold_time_bars | 6.8538 |
| exposure | 0.2536 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
