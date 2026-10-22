# EMA Hourly Continuation — WIF/USDT P21_26

**Symbol:** WIF/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1215 |
| net_profit_factor | 0.3791 |
| net_win_rate | 0.3835 |
| gross_profit_factor | 0.8189 |
| gross_win_rate | 0.4115 |
| sharpe_ratio | -12.9243 |
| sortino_ratio | -6.4452 |
| max_drawdown | 0.9998 |
| cagr | -0.9666 |
| net_avg_win | 13.1007 |
| net_avg_loss | -21.4993 |
| avg_hold_time_bars | 1.6733 |
| exposure | 0.0924 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
