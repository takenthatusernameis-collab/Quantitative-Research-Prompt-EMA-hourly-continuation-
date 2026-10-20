# EMA Hourly Continuation — NYM/USDT P26_144

**Symbol:** NYM/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 489 |
| net_profit_factor | 0.2981 |
| net_win_rate | 0.3538 |
| gross_profit_factor | 0.5509 |
| gross_win_rate | 0.3701 |
| sharpe_ratio | -7.5517 |
| sortino_ratio | -2.3486 |
| max_drawdown | 0.9524 |
| cagr | -0.7026 |
| net_avg_win | 23.3764 |
| net_avg_loss | -42.9373 |
| avg_hold_time_bars | 20.0307 |
| exposure | 0.4452 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
