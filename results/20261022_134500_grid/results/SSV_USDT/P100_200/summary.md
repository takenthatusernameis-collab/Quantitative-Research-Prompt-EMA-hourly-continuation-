# EMA Hourly Continuation — SSV/USDT P100_200

**Symbol:** SSV/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 434 |
| net_profit_factor | 0.5513 |
| net_win_rate | 0.4401 |
| gross_profit_factor | 0.8494 |
| gross_win_rate | 0.4470 |
| sharpe_ratio | -4.2713 |
| sortino_ratio | -1.2530 |
| max_drawdown | 0.7890 |
| cagr | -0.4500 |
| net_avg_win | 50.0987 |
| net_avg_loss | -71.4217 |
| avg_hold_time_bars | 8.6452 |
| exposure | 0.1698 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
