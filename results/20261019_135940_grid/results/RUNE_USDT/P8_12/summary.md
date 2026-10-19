# EMA Hourly Continuation — RUNE/USDT P8_12

**Symbol:** RUNE/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1804 |
| net_profit_factor | 0.1745 |
| net_win_rate | 0.3331 |
| gross_profit_factor | 0.6351 |
| gross_win_rate | 0.4013 |
| sharpe_ratio | -19.5614 |
| sortino_ratio | -12.2747 |
| max_drawdown | 1.0000 |
| cagr | -0.9987 |
| net_avg_win | 3.5176 |
| net_avg_loss | -10.0699 |
| avg_hold_time_bars | 1.6624 |
| exposure | 0.1363 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
