# EMA Hourly Continuation — CTC/USDT P21_200

**Symbol:** CTC/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 370 |
| net_profit_factor | 0.8087 |
| net_win_rate | 0.5081 |
| gross_profit_factor | 1.0192 |
| gross_win_rate | 0.5081 |
| sharpe_ratio | -1.2410 |
| sortino_ratio | -0.3415 |
| max_drawdown | 0.4419 |
| cagr | -0.1471 |
| net_avg_win | 74.1106 |
| net_avg_loss | -94.6577 |
| avg_hold_time_bars | 33.8946 |
| exposure | 0.5700 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
