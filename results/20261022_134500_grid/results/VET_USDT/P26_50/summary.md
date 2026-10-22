# EMA Hourly Continuation — VET/USDT P26_50

**Symbol:** VET/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 954 |
| net_profit_factor | 0.4325 |
| net_win_rate | 0.4560 |
| gross_profit_factor | 0.9062 |
| gross_win_rate | 0.4748 |
| sharpe_ratio | -8.1029 |
| sortino_ratio | -3.5394 |
| max_drawdown | 0.9887 |
| cagr | -0.8293 |
| net_avg_win | 17.3132 |
| net_avg_loss | -33.5514 |
| avg_hold_time_bars | 3.3585 |
| exposure | 0.1456 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
