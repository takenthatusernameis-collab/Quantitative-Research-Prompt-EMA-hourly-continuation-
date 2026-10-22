# EMA Hourly Continuation — SLP/USDT P34_100

**Symbol:** SLP/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 502 |
| net_profit_factor | 0.8141 |
| net_win_rate | 0.5100 |
| gross_profit_factor | 1.0639 |
| gross_win_rate | 0.5100 |
| sharpe_ratio | -1.6416 |
| sortino_ratio | -0.5281 |
| max_drawdown | 0.4964 |
| cagr | -0.2169 |
| net_avg_win | 78.4738 |
| net_avg_loss | -100.3122 |
| avg_hold_time_bars | 11.5458 |
| exposure | 0.2635 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
