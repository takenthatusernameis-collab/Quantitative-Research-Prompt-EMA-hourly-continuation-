# EMA Hourly Continuation — HBAR/USDT P20_50

**Symbol:** HBAR/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 464 |
| net_profit_factor | 0.7672 |
| net_win_rate | 0.5172 |
| gross_profit_factor | 1.0660 |
| gross_win_rate | 0.5172 |
| sharpe_ratio | -1.8060 |
| sortino_ratio | -0.5604 |
| max_drawdown | 0.4923 |
| cagr | -0.2259 |
| net_avg_win | 65.1345 |
| net_avg_loss | -90.9603 |
| avg_hold_time_bars | 7.8664 |
| exposure | 0.1659 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
