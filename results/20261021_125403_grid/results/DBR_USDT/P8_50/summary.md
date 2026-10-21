# EMA Hourly Continuation — DBR/USDT P8_50

**Symbol:** DBR/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 529 |
| net_profit_factor | 0.7236 |
| net_win_rate | 0.4896 |
| gross_profit_factor | 0.9862 |
| gross_win_rate | 0.4915 |
| sharpe_ratio | -2.8746 |
| sortino_ratio | -1.0571 |
| max_drawdown | 0.6521 |
| cagr | -0.3835 |
| net_avg_win | 62.7983 |
| net_avg_loss | -83.2496 |
| avg_hold_time_bars | 14.4159 |
| exposure | 0.4337 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
