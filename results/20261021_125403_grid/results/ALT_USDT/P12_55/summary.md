# EMA Hourly Continuation — ALT/USDT P12_55

**Symbol:** ALT/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 670 |
| net_profit_factor | 0.7069 |
| net_win_rate | 0.4627 |
| gross_profit_factor | 0.8855 |
| gross_win_rate | 0.4627 |
| sharpe_ratio | -3.1437 |
| sortino_ratio | -1.1563 |
| max_drawdown | 0.7533 |
| cagr | -0.4127 |
| net_avg_win | 57.3572 |
| net_avg_loss | -69.8706 |
| avg_hold_time_bars | 12.3851 |
| exposure | 0.3772 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
