# EMA Hourly Continuation — CHZ/USDT P20_26

**Symbol:** CHZ/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 191 |
| net_profit_factor | 0.6683 |
| net_win_rate | 0.4921 |
| gross_profit_factor | 0.9612 |
| gross_win_rate | 0.4921 |
| sharpe_ratio | -1.6927 |
| sortino_ratio | -0.3361 |
| max_drawdown | 0.3536 |
| cagr | -0.1419 |
| net_avg_win | 68.4019 |
| net_avg_loss | -99.1869 |
| avg_hold_time_bars | 4.7958 |
| exposure | 0.0416 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
