# EMA Hourly Continuation — KAS/USDT P12_34

**Symbol:** KAS/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 570 |
| net_profit_factor | 0.8393 |
| net_win_rate | 0.5333 |
| gross_profit_factor | 1.1278 |
| gross_win_rate | 0.5333 |
| sharpe_ratio | -1.2478 |
| sortino_ratio | -0.4307 |
| max_drawdown | 0.4486 |
| cagr | -0.1810 |
| net_avg_win | 67.7463 |
| net_avg_loss | -92.2491 |
| avg_hold_time_bars | 6.7474 |
| exposure | 0.1748 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
