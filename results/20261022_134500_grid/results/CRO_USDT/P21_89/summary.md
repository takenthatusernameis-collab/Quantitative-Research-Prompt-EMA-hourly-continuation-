# EMA Hourly Continuation — CRO/USDT P21_89

**Symbol:** CRO/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 740 |
| net_profit_factor | 0.4565 |
| net_win_rate | 0.4351 |
| gross_profit_factor | 0.8997 |
| gross_win_rate | 0.4595 |
| sharpe_ratio | -7.0244 |
| sortino_ratio | -2.6687 |
| max_drawdown | 0.9694 |
| cagr | -0.7423 |
| net_avg_win | 25.2177 |
| net_avg_loss | -42.5553 |
| avg_hold_time_bars | 11.6595 |
| exposure | 0.3922 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
