# EMA Hourly Continuation — ALT/USDT P26_34

**Symbol:** ALT/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 376 |
| net_profit_factor | 0.6338 |
| net_win_rate | 0.4787 |
| gross_profit_factor | 0.9156 |
| gross_win_rate | 0.4814 |
| sharpe_ratio | -2.7278 |
| sortino_ratio | -0.7568 |
| max_drawdown | 0.6047 |
| cagr | -0.2935 |
| net_avg_win | 55.9776 |
| net_avg_loss | -81.1076 |
| avg_hold_time_bars | 5.4096 |
| exposure | 0.0925 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
