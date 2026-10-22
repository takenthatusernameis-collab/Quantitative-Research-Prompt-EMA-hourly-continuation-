# EMA Hourly Continuation — SLP/USDT P12_50

**Symbol:** SLP/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 719 |
| net_profit_factor | 0.7177 |
| net_win_rate | 0.4757 |
| gross_profit_factor | 0.9363 |
| gross_win_rate | 0.4757 |
| sharpe_ratio | -3.1353 |
| sortino_ratio | -1.2000 |
| max_drawdown | 0.7572 |
| cagr | -0.4233 |
| net_avg_win | 55.6769 |
| net_avg_loss | -70.3752 |
| avg_hold_time_bars | 9.1474 |
| exposure | 0.2990 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
