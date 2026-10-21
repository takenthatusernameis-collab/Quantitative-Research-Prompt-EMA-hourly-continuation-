# EMA Hourly Continuation — T/USDT P21_200

**Symbol:** T/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 328 |
| net_profit_factor | 0.7566 |
| net_win_rate | 0.4970 |
| gross_profit_factor | 0.9827 |
| gross_win_rate | 0.4970 |
| sharpe_ratio | -1.5827 |
| sortino_ratio | -0.4078 |
| max_drawdown | 0.3815 |
| cagr | -0.1721 |
| net_avg_win | 72.2738 |
| net_avg_loss | -94.3676 |
| avg_hold_time_bars | 39.4634 |
| exposure | 0.5858 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
