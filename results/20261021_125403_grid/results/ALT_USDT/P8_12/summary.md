# EMA Hourly Continuation — ALT/USDT P8_12

**Symbol:** ALT/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 517 |
| net_profit_factor | 0.6779 |
| net_win_rate | 0.4874 |
| gross_profit_factor | 0.9854 |
| gross_win_rate | 0.4874 |
| sharpe_ratio | -3.0851 |
| sortino_ratio | -1.0053 |
| max_drawdown | 0.6988 |
| cagr | -0.3699 |
| net_avg_win | 57.3256 |
| net_avg_loss | -80.4191 |
| avg_hold_time_bars | 5.2340 |
| exposure | 0.1230 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
