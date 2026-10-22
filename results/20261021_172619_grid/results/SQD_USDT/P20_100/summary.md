# EMA Hourly Continuation — SQD/USDT P20_100

**Symbol:** SQD/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 481 |
| net_profit_factor | 0.8717 |
| net_win_rate | 0.5073 |
| gross_profit_factor | 1.0252 |
| gross_win_rate | 0.5073 |
| sharpe_ratio | -0.9376 |
| sortino_ratio | -0.2999 |
| max_drawdown | 0.3536 |
| cagr | -0.1324 |
| net_avg_win | 81.1816 |
| net_avg_loss | -95.8854 |
| avg_hold_time_bars | 16.7006 |
| exposure | 0.3776 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
