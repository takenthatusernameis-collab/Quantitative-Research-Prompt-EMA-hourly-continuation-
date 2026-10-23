# EMA Hourly Continuation — KSM/USDT P144_200

**Symbol:** KSM/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 415 |
| net_profit_factor | 0.5137 |
| net_win_rate | 0.4627 |
| gross_profit_factor | 0.9485 |
| gross_win_rate | 0.4795 |
| sharpe_ratio | -4.5515 |
| sortino_ratio | -1.3076 |
| max_drawdown | 0.8072 |
| cagr | -0.4745 |
| net_avg_win | 44.0884 |
| net_avg_loss | -73.8925 |
| avg_hold_time_bars | 4.4916 |
| exposure | 0.0847 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
