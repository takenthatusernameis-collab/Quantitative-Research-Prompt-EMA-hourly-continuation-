# EMA Hourly Continuation — KSM/USDT P20_34

**Symbol:** KSM/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1150 |
| net_profit_factor | 0.3441 |
| net_win_rate | 0.4104 |
| gross_profit_factor | 0.8132 |
| gross_win_rate | 0.4435 |
| sharpe_ratio | -10.8332 |
| sortino_ratio | -5.2598 |
| max_drawdown | 0.9987 |
| cagr | -0.9281 |
| net_avg_win | 11.0978 |
| net_avg_loss | -22.4553 |
| avg_hold_time_bars | 2.8000 |
| exposure | 0.1464 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
