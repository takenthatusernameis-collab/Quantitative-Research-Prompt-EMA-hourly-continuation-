# EMA Hourly Continuation — ALPINE/USDT P34_200

**Symbol:** ALPINE/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 391 |
| net_profit_factor | 0.6619 |
| net_win_rate | 0.4834 |
| gross_profit_factor | 0.9635 |
| gross_win_rate | 0.4910 |
| sharpe_ratio | -2.6799 |
| sortino_ratio | -0.7499 |
| max_drawdown | 0.6015 |
| cagr | -0.2960 |
| net_avg_win | 60.6770 |
| net_avg_loss | -85.7746 |
| avg_hold_time_bars | 31.0281 |
| exposure | 0.5515 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
