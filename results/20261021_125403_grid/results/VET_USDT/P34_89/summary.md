# EMA Hourly Continuation — VET/USDT P34_89

**Symbol:** VET/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 426 |
| net_profit_factor | 0.7197 |
| net_win_rate | 0.4977 |
| gross_profit_factor | 0.9626 |
| gross_win_rate | 0.4977 |
| sharpe_ratio | -1.9796 |
| sortino_ratio | -0.5854 |
| max_drawdown | 0.5375 |
| cagr | -0.2355 |
| net_avg_win | 59.4201 |
| net_avg_loss | -81.7875 |
| avg_hold_time_bars | 10.8826 |
| exposure | 0.2107 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
