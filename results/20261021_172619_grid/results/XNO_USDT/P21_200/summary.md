# EMA Hourly Continuation — XNO/USDT P21_200

**Symbol:** XNO/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 400 |
| net_profit_factor | 0.7144 |
| net_win_rate | 0.4600 |
| gross_profit_factor | 0.8670 |
| gross_win_rate | 0.4600 |
| sharpe_ratio | -2.2361 |
| sortino_ratio | -0.6349 |
| max_drawdown | 0.5206 |
| cagr | -0.2538 |
| net_avg_win | 70.7726 |
| net_avg_loss | -84.3906 |
| avg_hold_time_bars | 30.4150 |
| exposure | 0.5530 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
