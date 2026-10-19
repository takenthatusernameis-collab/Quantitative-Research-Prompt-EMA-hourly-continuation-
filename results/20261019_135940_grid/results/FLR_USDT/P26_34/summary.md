# EMA Hourly Continuation — FLR/USDT P26_34

**Symbol:** FLR/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1265 |
| net_profit_factor | 0.2508 |
| net_win_rate | 0.3209 |
| gross_profit_factor | 0.7418 |
| gross_win_rate | 0.3755 |
| sharpe_ratio | -16.6102 |
| sortino_ratio | -8.7256 |
| max_drawdown | 1.0000 |
| cagr | -0.9911 |
| net_avg_win | 8.2437 |
| net_avg_loss | -15.5377 |
| avg_hold_time_bars | 2.1312 |
| exposure | 0.1225 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
