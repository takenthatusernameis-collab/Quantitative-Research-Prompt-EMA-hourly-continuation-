# EMA Hourly Continuation — NOT/USDT P12_100

**Symbol:** NOT/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 416 |
| net_profit_factor | 0.8971 |
| net_win_rate | 0.5192 |
| gross_profit_factor | 1.0679 |
| gross_win_rate | 0.5192 |
| sharpe_ratio | -0.6491 |
| sortino_ratio | -0.1937 |
| max_drawdown | 0.2303 |
| cagr | -0.0892 |
| net_avg_win | 81.9496 |
| net_avg_loss | -98.6625 |
| avg_hold_time_bars | 28.9183 |
| exposure | 0.5651 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
