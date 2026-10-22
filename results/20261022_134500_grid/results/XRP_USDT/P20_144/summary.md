# EMA Hourly Continuation — XRP/USDT P20_144

**Symbol:** XRP/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 544 |
| net_profit_factor | 0.5142 |
| net_win_rate | 0.4651 |
| gross_profit_factor | 0.9884 |
| gross_win_rate | 0.4816 |
| sharpe_ratio | -5.1694 |
| sortino_ratio | -1.6672 |
| max_drawdown | 0.8938 |
| cagr | -0.5762 |
| net_avg_win | 36.9921 |
| net_avg_loss | -62.5465 |
| avg_hold_time_bars | 21.0919 |
| exposure | 0.5215 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
