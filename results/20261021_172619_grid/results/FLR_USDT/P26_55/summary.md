# EMA Hourly Continuation — FLR/USDT P26_55

**Symbol:** FLR/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 469 |
| net_profit_factor | 0.5654 |
| net_win_rate | 0.4414 |
| gross_profit_factor | 0.8120 |
| gross_win_rate | 0.4435 |
| sharpe_ratio | -4.1485 |
| sortino_ratio | -1.2830 |
| max_drawdown | 0.7957 |
| cagr | -0.4451 |
| net_avg_win | 48.5250 |
| net_avg_loss | -67.8090 |
| avg_hold_time_bars | 6.9872 |
| exposure | 0.1490 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
