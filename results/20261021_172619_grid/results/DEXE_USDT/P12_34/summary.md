# EMA Hourly Continuation — DEXE/USDT P12_34

**Symbol:** DEXE/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 540 |
| net_profit_factor | 0.6907 |
| net_win_rate | 0.4926 |
| gross_profit_factor | 0.9430 |
| gross_win_rate | 0.4926 |
| sharpe_ratio | -2.4172 |
| sortino_ratio | -0.8044 |
| max_drawdown | 0.6117 |
| cagr | -0.3087 |
| net_avg_win | 50.7297 |
| net_avg_loss | -71.3024 |
| avg_hold_time_bars | 11.5074 |
| exposure | 0.2825 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
