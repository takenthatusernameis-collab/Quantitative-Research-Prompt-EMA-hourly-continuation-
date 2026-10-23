# EMA Hourly Continuation — ETN/USDT P50_89

**Symbol:** ETN/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 690 |
| net_profit_factor | 0.2739 |
| net_win_rate | 0.3217 |
| gross_profit_factor | 0.4491 |
| gross_win_rate | 0.3435 |
| sharpe_ratio | -10.9359 |
| sortino_ratio | -4.4548 |
| max_drawdown | 0.9917 |
| cagr | -0.8959 |
| net_avg_win | 16.8476 |
| net_avg_loss | -29.1751 |
| avg_hold_time_bars | 4.0072 |
| exposure | 0.1502 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
