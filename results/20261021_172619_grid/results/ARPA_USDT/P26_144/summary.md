# EMA Hourly Continuation — ARPA/USDT P26_144

**Symbol:** ARPA/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 463 |
| net_profit_factor | 0.6986 |
| net_win_rate | 0.4752 |
| gross_profit_factor | 0.8974 |
| gross_win_rate | 0.4773 |
| sharpe_ratio | -2.3857 |
| sortino_ratio | -0.7300 |
| max_drawdown | 0.5946 |
| cagr | -0.2849 |
| net_avg_win | 60.1513 |
| net_avg_loss | -77.9508 |
| avg_hold_time_bars | 21.5810 |
| exposure | 0.4521 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
