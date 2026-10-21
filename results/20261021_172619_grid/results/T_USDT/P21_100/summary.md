# EMA Hourly Continuation — T/USDT P21_100

**Symbol:** T/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 477 |
| net_profit_factor | 0.7579 |
| net_win_rate | 0.5052 |
| gross_profit_factor | 1.0422 |
| gross_win_rate | 0.5052 |
| sharpe_ratio | -2.0517 |
| sortino_ratio | -0.6407 |
| max_drawdown | 0.5601 |
| cagr | -0.2549 |
| net_avg_win | 68.0663 |
| net_avg_loss | -91.7094 |
| avg_hold_time_bars | 18.0503 |
| exposure | 0.3896 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
