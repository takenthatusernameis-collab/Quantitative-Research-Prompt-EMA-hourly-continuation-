# EMA Hourly Continuation — YFI/USDT P21_89

**Symbol:** YFI/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 575 |
| net_profit_factor | 0.7067 |
| net_win_rate | 0.4870 |
| gross_profit_factor | 0.9942 |
| gross_win_rate | 0.4870 |
| sharpe_ratio | -2.9837 |
| sortino_ratio | -1.0213 |
| max_drawdown | 0.7170 |
| cagr | -0.3740 |
| net_avg_win | 59.6634 |
| net_avg_loss | -80.1281 |
| avg_hold_time_bars | 13.1583 |
| exposure | 0.3424 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
