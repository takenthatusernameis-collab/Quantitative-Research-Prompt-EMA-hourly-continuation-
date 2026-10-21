# EMA Hourly Continuation — SOL/USDT P12_26

**Symbol:** SOL/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 409 |
| net_profit_factor | 0.7636 |
| net_win_rate | 0.5208 |
| gross_profit_factor | 1.1003 |
| gross_win_rate | 0.5208 |
| sharpe_ratio | -1.8624 |
| sortino_ratio | -0.5435 |
| max_drawdown | 0.5145 |
| cagr | -0.2197 |
| net_avg_win | 70.3208 |
| net_avg_loss | -100.0731 |
| avg_hold_time_bars | 5.5917 |
| exposure | 0.1040 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
