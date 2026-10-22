# EMA Hourly Continuation — INJ/USDT P89_144

**Symbol:** INJ/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 489 |
| net_profit_factor | 0.4805 |
| net_win_rate | 0.4254 |
| gross_profit_factor | 0.7692 |
| gross_win_rate | 0.4294 |
| sharpe_ratio | -5.2513 |
| sortino_ratio | -1.6280 |
| max_drawdown | 0.8729 |
| cagr | -0.5528 |
| net_avg_win | 38.5767 |
| net_avg_loss | -59.4246 |
| avg_hold_time_bars | 4.6851 |
| exposure | 0.1041 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
