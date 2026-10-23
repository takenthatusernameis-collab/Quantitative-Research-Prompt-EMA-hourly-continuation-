# EMA Hourly Continuation — MOG/USDT P21_89

**Symbol:** MOG/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 634 |
| net_profit_factor | 0.7228 |
| net_win_rate | 0.4874 |
| gross_profit_factor | 0.9593 |
| gross_win_rate | 0.4874 |
| sharpe_ratio | -3.0985 |
| sortino_ratio | -1.1528 |
| max_drawdown | 0.7463 |
| cagr | -0.4203 |
| net_avg_win | 60.2520 |
| net_avg_loss | -79.2571 |
| avg_hold_time_bars | 12.1341 |
| exposure | 0.3824 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
