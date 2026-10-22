# EMA Hourly Continuation — WOO/USDT P89_144

**Symbol:** WOO/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 281 |
| net_profit_factor | 0.6715 |
| net_win_rate | 0.4733 |
| gross_profit_factor | 0.8982 |
| gross_win_rate | 0.4733 |
| sharpe_ratio | -2.1303 |
| sortino_ratio | -0.5100 |
| max_drawdown | 0.4446 |
| cagr | -0.2088 |
| net_avg_win | 68.3298 |
| net_avg_loss | -91.4453 |
| avg_hold_time_bars | 7.1103 |
| exposure | 0.0908 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
