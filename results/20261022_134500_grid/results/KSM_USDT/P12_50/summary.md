# EMA Hourly Continuation — KSM/USDT P12_50

**Symbol:** KSM/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1037 |
| net_profit_factor | 0.5468 |
| net_win_rate | 0.4474 |
| gross_profit_factor | 0.9146 |
| gross_win_rate | 0.4619 |
| sharpe_ratio | -7.0614 |
| sortino_ratio | -3.1808 |
| max_drawdown | 0.9812 |
| cagr | -0.7921 |
| net_avg_win | 25.4974 |
| net_avg_loss | -37.7611 |
| avg_hold_time_bars | 7.8708 |
| exposure | 0.3710 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
