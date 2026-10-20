# EMA Hourly Continuation — G/USDT P21_144

**Symbol:** G/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 392 |
| net_profit_factor | 0.5325 |
| net_win_rate | 0.4286 |
| gross_profit_factor | 0.8078 |
| gross_win_rate | 0.4413 |
| sharpe_ratio | -4.2100 |
| sortino_ratio | -1.2611 |
| max_drawdown | 0.7554 |
| cagr | -0.4485 |
| net_avg_win | 49.1777 |
| net_avg_loss | -69.2604 |
| avg_hold_time_bars | 28.5255 |
| exposure | 0.5880 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
