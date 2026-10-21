# EMA Hourly Continuation — ALT/USDT P21_50

**Symbol:** ALT/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 581 |
| net_profit_factor | 0.6679 |
| net_win_rate | 0.4596 |
| gross_profit_factor | 0.8797 |
| gross_win_rate | 0.4596 |
| sharpe_ratio | -3.3847 |
| sortino_ratio | -1.1615 |
| max_drawdown | 0.7681 |
| cagr | -0.4135 |
| net_avg_win | 55.6024 |
| net_avg_loss | -70.7883 |
| avg_hold_time_bars | 7.6506 |
| exposure | 0.2020 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
