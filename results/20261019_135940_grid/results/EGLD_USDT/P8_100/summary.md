# EMA Hourly Continuation — EGLD/USDT P8_100

**Symbol:** EGLD/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 631 |
| net_profit_factor | 0.7028 |
| net_win_rate | 0.5103 |
| gross_profit_factor | 1.0739 |
| gross_win_rate | 0.5135 |
| sharpe_ratio | -2.8386 |
| sortino_ratio | -1.0010 |
| max_drawdown | 0.7257 |
| cagr | -0.3823 |
| net_avg_win | 51.5289 |
| net_avg_loss | -76.4074 |
| avg_hold_time_bars | 23.0967 |
| exposure | 0.6625 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
