# EMA Hourly Continuation — CKB/USDT P21_200

**Symbol:** CKB/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 333 |
| net_profit_factor | 0.7922 |
| net_win_rate | 0.4985 |
| gross_profit_factor | 0.9708 |
| gross_win_rate | 0.4985 |
| sharpe_ratio | -1.2524 |
| sortino_ratio | -0.3269 |
| max_drawdown | 0.3367 |
| cagr | -0.1408 |
| net_avg_win | 72.8079 |
| net_avg_loss | -91.3532 |
| avg_hold_time_bars | 39.6246 |
| exposure | 0.5998 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
