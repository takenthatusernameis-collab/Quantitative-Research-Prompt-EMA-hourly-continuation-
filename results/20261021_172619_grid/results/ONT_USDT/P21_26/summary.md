# EMA Hourly Continuation — ONT/USDT P21_26

**Symbol:** ONT/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 220 |
| net_profit_factor | 0.6649 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9854 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.8212 |
| sortino_ratio | -0.3877 |
| max_drawdown | 0.4023 |
| cagr | -0.1624 |
| net_avg_win | 65.0066 |
| net_avg_loss | -97.7746 |
| avg_hold_time_bars | 5.4818 |
| exposure | 0.0546 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
