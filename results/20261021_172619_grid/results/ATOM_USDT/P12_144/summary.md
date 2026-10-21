# EMA Hourly Continuation — ATOM/USDT P12_144

**Symbol:** ATOM/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 375 |
| net_profit_factor | 0.8699 |
| net_win_rate | 0.5200 |
| gross_profit_factor | 1.0764 |
| gross_win_rate | 0.5200 |
| sharpe_ratio | -0.8090 |
| sortino_ratio | -0.2254 |
| max_drawdown | 0.2549 |
| cagr | -0.1011 |
| net_avg_win | 80.4757 |
| net_avg_loss | -100.2226 |
| avg_hold_time_bars | 38.3440 |
| exposure | 0.6536 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
