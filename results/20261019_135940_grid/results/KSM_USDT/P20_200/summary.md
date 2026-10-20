# EMA Hourly Continuation — KSM/USDT P20_200

**Symbol:** KSM/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 354 |
| net_profit_factor | 0.6373 |
| net_win_rate | 0.4746 |
| gross_profit_factor | 0.9062 |
| gross_win_rate | 0.4774 |
| sharpe_ratio | -2.7205 |
| sortino_ratio | -0.7141 |
| max_drawdown | 0.6020 |
| cagr | -0.2942 |
| net_avg_win | 60.9978 |
| net_avg_loss | -86.4489 |
| avg_hold_time_bars | 40.9266 |
| exposure | 0.6585 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
