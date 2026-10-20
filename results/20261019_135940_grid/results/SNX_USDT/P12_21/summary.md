# EMA Hourly Continuation — SNX/USDT P12_21

**Symbol:** SNX/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1443 |
| net_profit_factor | 0.3181 |
| net_win_rate | 0.4207 |
| gross_profit_factor | 0.8345 |
| gross_win_rate | 0.4511 |
| sharpe_ratio | -12.0170 |
| sortino_ratio | -6.4551 |
| max_drawdown | 0.9998 |
| cagr | -0.9626 |
| net_avg_win | 7.6843 |
| net_avg_loss | -17.5381 |
| avg_hold_time_bars | 2.4705 |
| exposure | 0.1613 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
