# EMA Hourly Continuation — SAND/USDT P12_144

**Symbol:** SAND/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 400 |
| net_profit_factor | 0.6340 |
| net_win_rate | 0.4750 |
| gross_profit_factor | 0.9511 |
| gross_win_rate | 0.4800 |
| sharpe_ratio | -3.0650 |
| sortino_ratio | -0.8556 |
| max_drawdown | 0.6608 |
| cagr | -0.3410 |
| net_avg_win | 59.1833 |
| net_avg_loss | -84.4579 |
| avg_hold_time_bars | 39.8050 |
| exposure | 0.7237 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
