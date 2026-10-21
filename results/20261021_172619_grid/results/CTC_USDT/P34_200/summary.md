# EMA Hourly Continuation — CTC/USDT P34_200

**Symbol:** CTC/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 343 |
| net_profit_factor | 0.8685 |
| net_win_rate | 0.5277 |
| gross_profit_factor | 1.1039 |
| gross_win_rate | 0.5277 |
| sharpe_ratio | -0.7800 |
| sortino_ratio | -0.2077 |
| max_drawdown | 0.3260 |
| cagr | -0.0938 |
| net_avg_win | 79.9498 |
| net_avg_loss | -102.8559 |
| avg_hold_time_bars | 27.9329 |
| exposure | 0.4355 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
