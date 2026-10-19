# EMA Hourly Continuation — SUN/USDT P8_55

**Symbol:** SUN/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 900 |
| net_profit_factor | 0.3381 |
| net_win_rate | 0.3933 |
| gross_profit_factor | 0.8792 |
| gross_win_rate | 0.4400 |
| sharpe_ratio | -9.8863 |
| sortino_ratio | -4.1845 |
| max_drawdown | 0.9958 |
| cagr | -0.8858 |
| net_avg_win | 14.3667 |
| net_avg_loss | -27.5529 |
| avg_hold_time_bars | 12.7522 |
| exposure | 0.5194 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
