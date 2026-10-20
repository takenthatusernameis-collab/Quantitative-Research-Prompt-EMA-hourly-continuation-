# EMA Hourly Continuation — EDU/USDT P34_50

**Symbol:** EDU/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 951 |
| net_profit_factor | 0.3628 |
| net_win_rate | 0.4059 |
| gross_profit_factor | 0.6996 |
| gross_win_rate | 0.4185 |
| sharpe_ratio | -9.2608 |
| sortino_ratio | -4.0457 |
| max_drawdown | 0.9935 |
| cagr | -0.8626 |
| net_avg_win | 14.6507 |
| net_avg_loss | -27.5898 |
| avg_hold_time_bars | 3.1640 |
| exposure | 0.1362 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
