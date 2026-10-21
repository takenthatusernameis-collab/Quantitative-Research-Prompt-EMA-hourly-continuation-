# EMA Hourly Continuation — EWT/USDT P12_89

**Symbol:** EWT/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 517 |
| net_profit_factor | 0.6558 |
| net_win_rate | 0.4526 |
| gross_profit_factor | 0.8033 |
| gross_win_rate | 0.4526 |
| sharpe_ratio | -2.8324 |
| sortino_ratio | -0.9129 |
| max_drawdown | 0.6904 |
| cagr | -0.3435 |
| net_avg_win | 53.1254 |
| net_avg_loss | -66.9798 |
| avg_hold_time_bars | 16.1663 |
| exposure | 0.3799 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
