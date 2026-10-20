# EMA Hourly Continuation — SSV/USDT P26_144

**Symbol:** SSV/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 493 |
| net_profit_factor | 0.6372 |
| net_win_rate | 0.4625 |
| gross_profit_factor | 0.9211 |
| gross_win_rate | 0.4746 |
| sharpe_ratio | -3.4066 |
| sortino_ratio | -1.0623 |
| max_drawdown | 0.7298 |
| cagr | -0.3965 |
| net_avg_win | 55.4854 |
| net_avg_loss | -74.9173 |
| avg_hold_time_bars | 22.9351 |
| exposure | 0.5117 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
