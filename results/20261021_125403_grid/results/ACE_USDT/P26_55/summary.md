# EMA Hourly Continuation — ACE/USDT P26_55

**Symbol:** ACE/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 482 |
| net_profit_factor | 0.7343 |
| net_win_rate | 0.5104 |
| gross_profit_factor | 1.0139 |
| gross_win_rate | 0.5104 |
| sharpe_ratio | -1.9541 |
| sortino_ratio | -0.6143 |
| max_drawdown | 0.5197 |
| cagr | -0.2453 |
| net_avg_win | 57.0890 |
| net_avg_loss | -81.0442 |
| avg_hold_time_bars | 7.9274 |
| exposure | 0.1729 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
