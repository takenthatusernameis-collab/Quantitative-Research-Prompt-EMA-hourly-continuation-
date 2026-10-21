# EMA Hourly Continuation — SUI/USDT P21_34

**Symbol:** SUI/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 276 |
| net_profit_factor | 0.6693 |
| net_win_rate | 0.4746 |
| gross_profit_factor | 0.9016 |
| gross_win_rate | 0.4746 |
| sharpe_ratio | -2.1090 |
| sortino_ratio | -0.5009 |
| max_drawdown | 0.4718 |
| cagr | -0.2044 |
| net_avg_win | 67.4828 |
| net_avg_loss | -91.0963 |
| avg_hold_time_bars | 4.9855 |
| exposure | 0.0625 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
