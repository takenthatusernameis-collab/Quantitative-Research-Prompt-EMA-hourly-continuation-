# EMA Hourly Continuation — ZRX/USDT P89_200

**Symbol:** ZRX/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 323 |
| net_profit_factor | 0.8002 |
| net_win_rate | 0.5139 |
| gross_profit_factor | 1.0528 |
| gross_win_rate | 0.5139 |
| sharpe_ratio | -1.2560 |
| sortino_ratio | -0.3243 |
| max_drawdown | 0.3428 |
| cagr | -0.1396 |
| net_avg_win | 75.8588 |
| net_avg_loss | -100.2324 |
| avg_hold_time_bars | 12.6625 |
| exposure | 0.1859 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
