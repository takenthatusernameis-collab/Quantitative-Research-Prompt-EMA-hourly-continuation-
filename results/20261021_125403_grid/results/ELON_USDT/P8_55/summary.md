# EMA Hourly Continuation — ELON/USDT P8_55

**Symbol:** ELON/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 689 |
| net_profit_factor | 0.7388 |
| net_win_rate | 0.4790 |
| gross_profit_factor | 0.9357 |
| gross_win_rate | 0.4790 |
| sharpe_ratio | -2.7775 |
| sortino_ratio | -1.0400 |
| max_drawdown | 0.7102 |
| cagr | -0.3802 |
| net_avg_win | 59.9225 |
| net_avg_loss | -74.5589 |
| avg_hold_time_bars | 12.8447 |
| exposure | 0.4023 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
