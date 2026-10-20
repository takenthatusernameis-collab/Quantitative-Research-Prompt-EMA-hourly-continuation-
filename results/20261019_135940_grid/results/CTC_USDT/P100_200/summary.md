# EMA Hourly Continuation — CTC/USDT P100_200

**Symbol:** CTC/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 425 |
| net_profit_factor | 0.5902 |
| net_win_rate | 0.4753 |
| gross_profit_factor | 1.0705 |
| gross_win_rate | 0.4988 |
| sharpe_ratio | -3.8506 |
| sortino_ratio | -1.1190 |
| max_drawdown | 0.7602 |
| cagr | -0.4187 |
| net_avg_win | 53.0494 |
| net_avg_loss | -81.4156 |
| avg_hold_time_bars | 7.4376 |
| exposure | 0.1437 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
