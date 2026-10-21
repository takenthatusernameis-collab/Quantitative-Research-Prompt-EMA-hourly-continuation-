# EMA Hourly Continuation — CTC/USDT P21_55

**Symbol:** CTC/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 537 |
| net_profit_factor | 0.7437 |
| net_win_rate | 0.5140 |
| gross_profit_factor | 1.0506 |
| gross_win_rate | 0.5140 |
| sharpe_ratio | -2.0797 |
| sortino_ratio | -0.6928 |
| max_drawdown | 0.5698 |
| cagr | -0.2727 |
| net_avg_win | 57.8757 |
| net_avg_loss | -82.2963 |
| avg_hold_time_bars | 9.5177 |
| exposure | 0.2323 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
