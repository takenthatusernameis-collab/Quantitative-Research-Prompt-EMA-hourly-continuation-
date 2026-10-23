# EMA Hourly Continuation — MEME/USDT P12_21

**Symbol:** MEME/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1479 |
| net_profit_factor | 0.3416 |
| net_win_rate | 0.4124 |
| gross_profit_factor | 0.7905 |
| gross_win_rate | 0.4368 |
| sharpe_ratio | -11.8235 |
| sortino_ratio | -6.4490 |
| max_drawdown | 0.9997 |
| cagr | -0.9603 |
| net_avg_win | 8.5043 |
| net_avg_loss | -17.4736 |
| avg_hold_time_bars | 2.5247 |
| exposure | 0.1697 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
