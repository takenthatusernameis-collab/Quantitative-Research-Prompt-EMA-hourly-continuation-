# EMA Hourly Continuation — TAIKO/USDT P100_144

**Symbol:** TAIKO/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 175 |
| net_profit_factor | 0.7687 |
| net_win_rate | 0.5200 |
| gross_profit_factor | 1.0789 |
| gross_win_rate | 0.5200 |
| sharpe_ratio | -1.1129 |
| sortino_ratio | -0.2182 |
| max_drawdown | 0.2373 |
| cagr | -0.0950 |
| net_avg_win | 77.1603 |
| net_avg_loss | -108.7404 |
| avg_hold_time_bars | 7.3600 |
| exposure | 0.0619 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
