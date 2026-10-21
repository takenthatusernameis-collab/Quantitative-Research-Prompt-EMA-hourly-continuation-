# EMA Hourly Continuation — SLP/USDT P12_26

**Symbol:** SLP/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 550 |
| net_profit_factor | 0.6635 |
| net_win_rate | 0.4782 |
| gross_profit_factor | 0.9251 |
| gross_win_rate | 0.4782 |
| sharpe_ratio | -3.1271 |
| sortino_ratio | -1.0505 |
| max_drawdown | 0.7072 |
| cagr | -0.3809 |
| net_avg_win | 52.4774 |
| net_avg_loss | -72.4816 |
| avg_hold_time_bars | 5.3218 |
| exposure | 0.1330 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
