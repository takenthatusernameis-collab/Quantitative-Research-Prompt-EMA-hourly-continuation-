# EMA Hourly Continuation — T/USDT P55_100

**Symbol:** T/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 390 |
| net_profit_factor | 0.5668 |
| net_win_rate | 0.4641 |
| gross_profit_factor | 0.8428 |
| gross_win_rate | 0.4641 |
| sharpe_ratio | -3.3196 |
| sortino_ratio | -0.9356 |
| max_drawdown | 0.6721 |
| cagr | -0.3476 |
| net_avg_win | 47.6769 |
| net_avg_loss | -72.8420 |
| avg_hold_time_bars | 10.7385 |
| exposure | 0.1895 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
