# EMA Hourly Continuation — MINA/USDT P12_100

**Symbol:** MINA/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 493 |
| net_profit_factor | 0.8752 |
| net_win_rate | 0.5213 |
| gross_profit_factor | 1.0833 |
| gross_win_rate | 0.5213 |
| sharpe_ratio | -0.9214 |
| sortino_ratio | -0.2941 |
| max_drawdown | 0.4231 |
| cagr | -0.1302 |
| net_avg_win | 80.6399 |
| net_avg_loss | -100.3394 |
| avg_hold_time_bars | 26.2008 |
| exposure | 0.5871 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
