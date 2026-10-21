# EMA Hourly Continuation — SUPER/USDT P20_50

**Symbol:** SUPER/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 536 |
| net_profit_factor | 0.8141 |
| net_win_rate | 0.5205 |
| gross_profit_factor | 1.0837 |
| gross_win_rate | 0.5224 |
| sharpe_ratio | -1.5421 |
| sortino_ratio | -0.5132 |
| max_drawdown | 0.5068 |
| cagr | -0.2117 |
| net_avg_win | 70.5906 |
| net_avg_loss | -94.1340 |
| avg_hold_time_bars | 7.6269 |
| exposure | 0.1858 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
