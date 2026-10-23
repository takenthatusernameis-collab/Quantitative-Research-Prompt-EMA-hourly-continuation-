# EMA Hourly Continuation — SLP/USDT P100_200

**Symbol:** SLP/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 441 |
| net_profit_factor | 0.5054 |
| net_win_rate | 0.4467 |
| gross_profit_factor | 0.8086 |
| gross_win_rate | 0.4535 |
| sharpe_ratio | -4.3241 |
| sortino_ratio | -1.2774 |
| max_drawdown | 0.7931 |
| cagr | -0.4632 |
| net_avg_win | 40.9967 |
| net_avg_loss | -65.4911 |
| avg_hold_time_bars | 8.5578 |
| exposure | 0.1715 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
