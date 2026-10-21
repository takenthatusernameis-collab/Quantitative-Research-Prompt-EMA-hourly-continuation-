# EMA Hourly Continuation — XPR/USDT P20_34

**Symbol:** XPR/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 982 |
| net_profit_factor | 0.2426 |
| net_win_rate | 0.3635 |
| gross_profit_factor | 0.5996 |
| gross_win_rate | 0.3798 |
| sharpe_ratio | -13.0545 |
| sortino_ratio | -5.9030 |
| max_drawdown | 0.9997 |
| cagr | -0.9610 |
| net_avg_win | 8.9711 |
| net_avg_loss | -21.1196 |
| avg_hold_time_bars | 3.5794 |
| exposure | 0.1598 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
