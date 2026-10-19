# EMA Hourly Continuation — SKY/USDT P8_12

**Symbol:** SKY/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1385 |
| net_profit_factor | 0.1999 |
| net_win_rate | 0.3538 |
| gross_profit_factor | 0.8647 |
| gross_win_rate | 0.4245 |
| sharpe_ratio | -17.8582 |
| sortino_ratio | -10.7512 |
| max_drawdown | 1.0000 |
| cagr | -0.9966 |
| net_avg_win | 5.0997 |
| net_avg_loss | -13.9651 |
| avg_hold_time_bars | 2.0628 |
| exposure | 0.1593 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
