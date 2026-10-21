# EMA Hourly Continuation — JTO/USDT P26_34

**Symbol:** JTO/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 231 |
| net_profit_factor | 0.6661 |
| net_win_rate | 0.4762 |
| gross_profit_factor | 0.9086 |
| gross_win_rate | 0.4762 |
| sharpe_ratio | -1.9157 |
| sortino_ratio | -0.4165 |
| max_drawdown | 0.3977 |
| cagr | -0.1732 |
| net_avg_win | 68.8783 |
| net_avg_loss | -93.9979 |
| avg_hold_time_bars | 5.4069 |
| exposure | 0.0568 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
