# EMA Hourly Continuation — SWFTC/USDT P21_34

**Symbol:** SWFTC/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 256 |
| net_profit_factor | 0.6185 |
| net_win_rate | 0.4648 |
| gross_profit_factor | 0.8633 |
| gross_win_rate | 0.4648 |
| sharpe_ratio | -2.3436 |
| sortino_ratio | -0.5358 |
| max_drawdown | 0.4779 |
| cagr | -0.2176 |
| net_avg_win | 62.6595 |
| net_avg_loss | -88.0014 |
| avg_hold_time_bars | 6.7461 |
| exposure | 0.0785 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
