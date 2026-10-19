# EMA Hourly Continuation — ETC/USDT P8_200

**Symbol:** ETC/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 319 |
| net_profit_factor | 0.5101 |
| net_win_rate | 0.4232 |
| gross_profit_factor | 0.7656 |
| gross_win_rate | 0.4357 |
| sharpe_ratio | -3.6992 |
| sortino_ratio | -0.9227 |
| max_drawdown | 0.6892 |
| cagr | -0.3609 |
| net_avg_win | 52.0689 |
| net_avg_loss | -74.8908 |
| avg_hold_time_bars | 56.5737 |
| exposure | 0.8203 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
