# EMA Hourly Continuation — BTT/USDT P50_200

**Symbol:** BTT/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 349 |
| net_profit_factor | 0.4470 |
| net_win_rate | 0.4155 |
| gross_profit_factor | 0.9480 |
| gross_win_rate | 0.4670 |
| sharpe_ratio | -5.4778 |
| sortino_ratio | -1.4421 |
| max_drawdown | 0.8486 |
| cagr | -0.5250 |
| net_avg_win | 47.1545 |
| net_avg_loss | -74.9766 |
| avg_hold_time_bars | 27.2321 |
| exposure | 0.4320 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
