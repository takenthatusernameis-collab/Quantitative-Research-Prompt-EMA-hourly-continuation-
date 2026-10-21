# EMA Hourly Continuation — ZRO/USDT P21_34

**Symbol:** ZRO/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 265 |
| net_profit_factor | 0.7468 |
| net_win_rate | 0.4906 |
| gross_profit_factor | 0.9683 |
| gross_win_rate | 0.4906 |
| sharpe_ratio | -1.5834 |
| sortino_ratio | -0.3829 |
| max_drawdown | 0.4018 |
| cagr | -0.1615 |
| net_avg_win | 76.4511 |
| net_avg_loss | -98.5773 |
| avg_hold_time_bars | 5.1170 |
| exposure | 0.0664 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
