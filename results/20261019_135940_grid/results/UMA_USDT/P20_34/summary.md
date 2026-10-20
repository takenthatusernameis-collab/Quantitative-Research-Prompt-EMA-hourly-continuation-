# EMA Hourly Continuation — UMA/USDT P20_34

**Symbol:** UMA/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1099 |
| net_profit_factor | 0.3130 |
| net_win_rate | 0.4031 |
| gross_profit_factor | 0.7249 |
| gross_win_rate | 0.4331 |
| sharpe_ratio | -10.7732 |
| sortino_ratio | -5.0767 |
| max_drawdown | 0.9984 |
| cagr | -0.9226 |
| net_avg_win | 10.2666 |
| net_avg_loss | -22.1523 |
| avg_hold_time_bars | 3.7034 |
| exposure | 0.1850 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
