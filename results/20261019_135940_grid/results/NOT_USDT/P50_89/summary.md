# EMA Hourly Continuation — NOT/USDT P50_89

**Symbol:** NOT/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 678 |
| net_profit_factor | 0.5174 |
| net_win_rate | 0.4661 |
| gross_profit_factor | 0.8640 |
| gross_win_rate | 0.4705 |
| sharpe_ratio | -5.3531 |
| sortino_ratio | -1.9963 |
| max_drawdown | 0.9088 |
| cagr | -0.6217 |
| net_avg_win | 30.7323 |
| net_avg_loss | -51.8491 |
| avg_hold_time_bars | 4.5029 |
| exposure | 0.1434 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
