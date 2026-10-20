# EMA Hourly Continuation — DGB/USDT P20_34

**Symbol:** DGB/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1247 |
| net_profit_factor | 0.3439 |
| net_win_rate | 0.3753 |
| gross_profit_factor | 0.8055 |
| gross_win_rate | 0.4050 |
| sharpe_ratio | -12.8916 |
| sortino_ratio | -6.4723 |
| max_drawdown | 0.9998 |
| cagr | -0.9662 |
| net_avg_win | 11.1973 |
| net_avg_loss | -19.5613 |
| avg_hold_time_bars | 2.8941 |
| exposure | 0.1640 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
