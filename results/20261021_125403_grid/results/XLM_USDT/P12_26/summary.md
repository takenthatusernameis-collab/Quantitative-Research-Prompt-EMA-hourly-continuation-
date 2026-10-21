# EMA Hourly Continuation — XLM/USDT P12_26

**Symbol:** XLM/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 418 |
| net_profit_factor | 0.6621 |
| net_win_rate | 0.5024 |
| gross_profit_factor | 1.0103 |
| gross_win_rate | 0.5024 |
| sharpe_ratio | -2.5779 |
| sortino_ratio | -0.7594 |
| max_drawdown | 0.5940 |
| cagr | -0.2924 |
| net_avg_win | 54.1604 |
| net_avg_loss | -82.5851 |
| avg_hold_time_bars | 5.4282 |
| exposure | 0.1031 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
