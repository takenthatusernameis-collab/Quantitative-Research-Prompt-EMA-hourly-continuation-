# EMA Hourly Continuation — DODO/USDT P12_34

**Symbol:** DODO/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1295 |
| net_profit_factor | 0.4986 |
| net_win_rate | 0.4270 |
| gross_profit_factor | 0.8905 |
| gross_win_rate | 0.4425 |
| sharpe_ratio | -8.9718 |
| sortino_ratio | -4.5528 |
| max_drawdown | 0.9961 |
| cagr | -0.8893 |
| net_avg_win | 17.9138 |
| net_avg_loss | -26.7757 |
| avg_hold_time_bars | 4.4849 |
| exposure | 0.2628 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
