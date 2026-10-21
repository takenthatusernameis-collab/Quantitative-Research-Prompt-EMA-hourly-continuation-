# EMA Hourly Continuation — CTC/USDT P34_100

**Symbol:** CTC/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 448 |
| net_profit_factor | 0.7711 |
| net_win_rate | 0.5156 |
| gross_profit_factor | 1.0516 |
| gross_win_rate | 0.5156 |
| sharpe_ratio | -1.6697 |
| sortino_ratio | -0.5080 |
| max_drawdown | 0.4917 |
| cagr | -0.2089 |
| net_avg_win | 64.8520 |
| net_avg_loss | -89.5348 |
| avg_hold_time_bars | 12.0982 |
| exposure | 0.2464 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
