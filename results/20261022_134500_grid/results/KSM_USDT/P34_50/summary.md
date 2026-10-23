# EMA Hourly Continuation — KSM/USDT P34_50

**Symbol:** KSM/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 889 |
| net_profit_factor | 0.3616 |
| net_win_rate | 0.4274 |
| gross_profit_factor | 0.7968 |
| gross_win_rate | 0.4499 |
| sharpe_ratio | -9.1341 |
| sortino_ratio | -3.8999 |
| max_drawdown | 0.9928 |
| cagr | -0.8566 |
| net_avg_win | 14.7944 |
| net_avg_loss | -30.5416 |
| avg_hold_time_bars | 3.1024 |
| exposure | 0.1254 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
