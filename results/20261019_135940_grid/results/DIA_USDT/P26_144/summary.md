# EMA Hourly Continuation — DIA/USDT P26_144

**Symbol:** DIA/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 517 |
| net_profit_factor | 0.6533 |
| net_win_rate | 0.4778 |
| gross_profit_factor | 0.9324 |
| gross_win_rate | 0.4836 |
| sharpe_ratio | -3.0448 |
| sortino_ratio | -0.9789 |
| max_drawdown | 0.7167 |
| cagr | -0.3684 |
| net_avg_win | 52.3530 |
| net_avg_loss | -73.3094 |
| avg_hold_time_bars | 19.7582 |
| exposure | 0.4622 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
