# EMA Hourly Continuation — BNB/USDT P50_100

**Symbol:** BNB/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 354 |
| net_profit_factor | 0.5577 |
| net_win_rate | 0.5028 |
| gross_profit_factor | 1.0217 |
| gross_win_rate | 0.5028 |
| sharpe_ratio | -3.3952 |
| sortino_ratio | -0.9253 |
| max_drawdown | 0.6617 |
| cagr | -0.3432 |
| net_avg_win | 46.1858 |
| net_avg_loss | -83.7593 |
| avg_hold_time_bars | 8.2542 |
| exposure | 0.1328 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
