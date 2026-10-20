# EMA Hourly Continuation — BRETT/USDT P12_34

**Symbol:** BRETT/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1201 |
| net_profit_factor | 0.5860 |
| net_win_rate | 0.4654 |
| gross_profit_factor | 0.8882 |
| gross_win_rate | 0.4746 |
| sharpe_ratio | -6.4971 |
| sortino_ratio | -3.2595 |
| max_drawdown | 0.9760 |
| cagr | -0.7918 |
| net_avg_win | 24.7092 |
| net_avg_loss | -36.7148 |
| avg_hold_time_bars | 4.3938 |
| exposure | 0.2539 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
