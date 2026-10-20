# EMA Hourly Continuation — RPL/USDT P100_144

**Symbol:** RPL/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 422 |
| net_profit_factor | 0.5730 |
| net_win_rate | 0.4905 |
| gross_profit_factor | 0.9833 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -3.4392 |
| sortino_ratio | -1.0018 |
| max_drawdown | 0.6985 |
| cagr | -0.3763 |
| net_avg_win | 45.1198 |
| net_avg_loss | -75.8144 |
| avg_hold_time_bars | 5.5900 |
| exposure | 0.1068 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
