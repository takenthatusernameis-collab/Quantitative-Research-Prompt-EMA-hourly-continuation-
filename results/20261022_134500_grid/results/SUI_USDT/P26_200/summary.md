# EMA Hourly Continuation — SUI/USDT P26_200

**Symbol:** SUI/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 339 |
| net_profit_factor | 0.7750 |
| net_win_rate | 0.5103 |
| gross_profit_factor | 1.0482 |
| gross_win_rate | 0.5133 |
| sharpe_ratio | -1.4202 |
| sortino_ratio | -0.3715 |
| max_drawdown | 0.4207 |
| cagr | -0.1613 |
| net_avg_win | 71.0795 |
| net_avg_loss | -95.5865 |
| avg_hold_time_bars | 38.6755 |
| exposure | 0.5960 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
