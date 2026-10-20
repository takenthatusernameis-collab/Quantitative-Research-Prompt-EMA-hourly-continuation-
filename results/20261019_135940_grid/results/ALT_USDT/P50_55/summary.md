# EMA Hourly Continuation — ALT/USDT P50_55

**Symbol:** ALT/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 726 |
| net_profit_factor | 0.2748 |
| net_win_rate | 0.3636 |
| gross_profit_factor | 0.7620 |
| gross_win_rate | 0.4146 |
| sharpe_ratio | -10.3799 |
| sortino_ratio | -4.0071 |
| max_drawdown | 0.9951 |
| cagr | -0.8786 |
| net_avg_win | 14.2842 |
| net_avg_loss | -29.6988 |
| avg_hold_time_bars | 3.2410 |
| exposure | 0.1070 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
