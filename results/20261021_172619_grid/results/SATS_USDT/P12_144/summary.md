# EMA Hourly Continuation — SATS/USDT P12_144

**Symbol:** SATS/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 401 |
| net_profit_factor | 0.6485 |
| net_win_rate | 0.4364 |
| gross_profit_factor | 0.7826 |
| gross_win_rate | 0.4389 |
| sharpe_ratio | -2.7391 |
| sortino_ratio | -0.7726 |
| max_drawdown | 0.6080 |
| cagr | -0.3009 |
| net_avg_win | 62.6737 |
| net_avg_loss | -74.8404 |
| avg_hold_time_bars | 34.8429 |
| exposure | 0.6322 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
