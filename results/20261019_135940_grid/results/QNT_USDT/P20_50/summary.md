# EMA Hourly Continuation — QNT/USDT P20_50

**Symbol:** QNT/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1137 |
| net_profit_factor | 0.3410 |
| net_win_rate | 0.4327 |
| gross_profit_factor | 0.7472 |
| gross_win_rate | 0.4565 |
| sharpe_ratio | -9.5667 |
| sortino_ratio | -4.5533 |
| max_drawdown | 0.9969 |
| cagr | -0.8994 |
| net_avg_win | 10.4859 |
| net_avg_loss | -23.4539 |
| avg_hold_time_bars | 3.8962 |
| exposure | 0.2014 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
