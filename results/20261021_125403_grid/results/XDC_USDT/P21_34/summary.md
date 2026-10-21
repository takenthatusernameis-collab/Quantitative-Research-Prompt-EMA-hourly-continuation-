# EMA Hourly Continuation — XDC/USDT P21_34

**Symbol:** XDC/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 266 |
| net_profit_factor | 0.5350 |
| net_win_rate | 0.4812 |
| gross_profit_factor | 0.8929 |
| gross_win_rate | 0.4812 |
| sharpe_ratio | -2.9214 |
| sortino_ratio | -0.6869 |
| max_drawdown | 0.5463 |
| cagr | -0.2683 |
| net_avg_win | 48.8753 |
| net_avg_loss | -84.7330 |
| avg_hold_time_bars | 6.6579 |
| exposure | 0.0805 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
