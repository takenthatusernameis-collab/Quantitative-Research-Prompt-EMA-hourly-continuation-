# EMA Hourly Continuation — YGG/USDT P21_144

**Symbol:** YGG/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 415 |
| net_profit_factor | 0.8308 |
| net_win_rate | 0.4988 |
| gross_profit_factor | 0.9997 |
| gross_win_rate | 0.4988 |
| sharpe_ratio | -1.2462 |
| sortino_ratio | -0.3621 |
| max_drawdown | 0.4015 |
| cagr | -0.1556 |
| net_avg_win | 82.3634 |
| net_avg_loss | -98.6646 |
| avg_hold_time_bars | 27.6458 |
| exposure | 0.5192 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
