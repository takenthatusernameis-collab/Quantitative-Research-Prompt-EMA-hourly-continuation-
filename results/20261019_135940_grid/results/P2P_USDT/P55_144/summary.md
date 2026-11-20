# EMA Hourly Continuation — P2P/USDT P55_144

**Symbol:** P2P/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 455 |
| net_profit_factor | 0.5249 |
| net_win_rate | 0.4132 |
| gross_profit_factor | 0.7044 |
| gross_win_rate | 0.4132 |
| sharpe_ratio | -4.1068 |
| sortino_ratio | -1.2280 |
| max_drawdown | 0.7728 |
| cagr | -0.4438 |
| net_avg_win | 45.2885 |
| net_avg_loss | -60.7564 |
| avg_hold_time_bars | 11.2154 |
| exposure | 0.2320 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
