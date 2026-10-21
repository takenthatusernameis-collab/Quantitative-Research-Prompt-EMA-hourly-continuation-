# EMA Hourly Continuation — BTT/USDT P8_34

**Symbol:** BTT/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 704 |
| net_profit_factor | 0.5326 |
| net_win_rate | 0.4503 |
| gross_profit_factor | 0.8670 |
| gross_win_rate | 0.4517 |
| sharpe_ratio | -6.1536 |
| sortino_ratio | -2.3483 |
| max_drawdown | 0.9370 |
| cagr | -0.6650 |
| net_avg_win | 33.6409 |
| net_avg_loss | -51.7383 |
| avg_hold_time_bars | 9.9631 |
| exposure | 0.3188 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
