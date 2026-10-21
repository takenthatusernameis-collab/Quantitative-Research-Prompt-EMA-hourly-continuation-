# EMA Hourly Continuation — DCR/USDT P55_100

**Symbol:** DCR/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 387 |
| net_profit_factor | 0.5940 |
| net_win_rate | 0.4625 |
| gross_profit_factor | 0.8436 |
| gross_win_rate | 0.4625 |
| sharpe_ratio | -3.0288 |
| sortino_ratio | -0.8483 |
| max_drawdown | 0.6446 |
| cagr | -0.3230 |
| net_avg_win | 51.1891 |
| net_avg_loss | -74.1583 |
| avg_hold_time_bars | 8.3023 |
| exposure | 0.1454 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
