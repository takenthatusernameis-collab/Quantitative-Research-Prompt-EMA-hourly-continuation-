# EMA Hourly Continuation — ENJ/USDT P26_50

**Symbol:** ENJ/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 995 |
| net_profit_factor | 0.5191 |
| net_win_rate | 0.4643 |
| gross_profit_factor | 1.0378 |
| gross_win_rate | 0.4834 |
| sharpe_ratio | -7.4903 |
| sortino_ratio | -3.3333 |
| max_drawdown | 0.9846 |
| cagr | -0.8068 |
| net_avg_win | 22.9980 |
| net_avg_loss | -38.3997 |
| avg_hold_time_bars | 3.4613 |
| exposure | 0.1558 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
