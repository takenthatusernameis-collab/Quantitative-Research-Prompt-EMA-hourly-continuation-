# EMA Hourly Continuation — HTR/USDT P34_100

**Symbol:** HTR/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 724 |
| net_profit_factor | 0.4742 |
| net_win_rate | 0.4157 |
| gross_profit_factor | 0.7211 |
| gross_win_rate | 0.4268 |
| sharpe_ratio | -6.5239 |
| sortino_ratio | -2.4625 |
| max_drawdown | 0.9539 |
| cagr | -0.7005 |
| net_avg_win | 28.5149 |
| net_avg_loss | -42.7868 |
| avg_hold_time_bars | 8.8204 |
| exposure | 0.2903 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
