# EMA Hourly Continuation — CTC/USDT P8_26

**Symbol:** CTC/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 739 |
| net_profit_factor | 0.6965 |
| net_win_rate | 0.5034 |
| gross_profit_factor | 1.0024 |
| gross_win_rate | 0.5034 |
| sharpe_ratio | -2.9728 |
| sortino_ratio | -1.1610 |
| max_drawdown | 0.7437 |
| cagr | -0.4115 |
| net_avg_win | 45.3899 |
| net_avg_loss | -66.0611 |
| avg_hold_time_bars | 7.2720 |
| exposure | 0.2443 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
