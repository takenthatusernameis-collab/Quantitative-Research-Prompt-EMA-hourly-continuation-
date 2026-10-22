# EMA Hourly Continuation — JUP/USDT P20_26

**Symbol:** JUP/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1203 |
| net_profit_factor | 0.3336 |
| net_win_rate | 0.3940 |
| gross_profit_factor | 0.8744 |
| gross_win_rate | 0.4281 |
| sharpe_ratio | -12.6619 |
| sortino_ratio | -6.3315 |
| max_drawdown | 0.9997 |
| cagr | -0.9619 |
| net_avg_win | 10.5603 |
| net_avg_loss | -20.5800 |
| avg_hold_time_bars | 1.7539 |
| exposure | 0.0959 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
