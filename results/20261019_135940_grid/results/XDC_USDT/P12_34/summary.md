# EMA Hourly Continuation — XDC/USDT P12_34

**Symbol:** XDC/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1321 |
| net_profit_factor | 0.1788 |
| net_win_rate | 0.3649 |
| gross_profit_factor | 0.5379 |
| gross_win_rate | 0.4300 |
| sharpe_ratio | -14.2008 |
| sortino_ratio | -7.4176 |
| max_drawdown | 0.9999 |
| cagr | -0.9799 |
| net_avg_win | 4.5159 |
| net_avg_loss | -14.5127 |
| avg_hold_time_bars | 4.1347 |
| exposure | 0.2483 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
