# EMA Hourly Continuation — SLP/USDT P21_89

**Symbol:** SLP/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 808 |
| net_profit_factor | 0.6200 |
| net_win_rate | 0.4530 |
| gross_profit_factor | 0.9594 |
| gross_win_rate | 0.4592 |
| sharpe_ratio | -5.4880 |
| sortino_ratio | -2.1904 |
| max_drawdown | 0.9325 |
| cagr | -0.6543 |
| net_avg_win | 41.4872 |
| net_avg_loss | -55.4077 |
| avg_hold_time_bars | 10.8552 |
| exposure | 0.3987 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
