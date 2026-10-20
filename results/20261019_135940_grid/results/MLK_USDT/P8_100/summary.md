# EMA Hourly Continuation — MLK/USDT P8_100

**Symbol:** MLK/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1016 |
| net_profit_factor | 0.4009 |
| net_win_rate | 0.3346 |
| gross_profit_factor | 0.6661 |
| gross_win_rate | 0.3435 |
| sharpe_ratio | -11.2278 |
| sortino_ratio | -5.0398 |
| max_drawdown | 0.9984 |
| cagr | -0.9218 |
| net_avg_win | 19.6521 |
| net_avg_loss | -24.6532 |
| avg_hold_time_bars | 12.4764 |
| exposure | 0.5737 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
