# EMA Hourly Continuation — SOL/USDT P12_26

**Symbol:** SOL/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1341 |
| net_profit_factor | 0.3744 |
| net_win_rate | 0.4094 |
| gross_profit_factor | 0.9476 |
| gross_win_rate | 0.4459 |
| sharpe_ratio | -12.3617 |
| sortino_ratio | -6.4300 |
| max_drawdown | 0.9998 |
| cagr | -0.9644 |
| net_avg_win | 10.8980 |
| net_avg_loss | -20.1777 |
| avg_hold_time_bars | 2.9314 |
| exposure | 0.1787 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
