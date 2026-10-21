# EMA Hourly Continuation — BAT/USDT P21_55

**Symbol:** BAT/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 606 |
| net_profit_factor | 0.6539 |
| net_win_rate | 0.4818 |
| gross_profit_factor | 0.9474 |
| gross_win_rate | 0.4818 |
| sharpe_ratio | -3.3597 |
| sortino_ratio | -1.1838 |
| max_drawdown | 0.7525 |
| cagr | -0.4189 |
| net_avg_win | 48.1438 |
| net_avg_loss | -68.4702 |
| avg_hold_time_bars | 8.4736 |
| exposure | 0.2334 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
