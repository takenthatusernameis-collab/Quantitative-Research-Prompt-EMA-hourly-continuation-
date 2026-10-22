# EMA Hourly Continuation — INJ/USDT P26_55

**Symbol:** INJ/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 906 |
| net_profit_factor | 0.5525 |
| net_win_rate | 0.4713 |
| gross_profit_factor | 0.9286 |
| gross_win_rate | 0.4757 |
| sharpe_ratio | -5.9931 |
| sortino_ratio | -2.5436 |
| max_drawdown | 0.9556 |
| cagr | -0.7095 |
| net_avg_win | 27.6128 |
| net_avg_loss | -44.5553 |
| avg_hold_time_bars | 4.2296 |
| exposure | 0.1742 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
