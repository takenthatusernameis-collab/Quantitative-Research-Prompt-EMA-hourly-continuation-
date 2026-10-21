# EMA Hourly Continuation — ROSE/USDT P12_144

**Symbol:** ROSE/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 325 |
| net_profit_factor | 1.0392 |
| net_win_rate | 0.5538 |
| gross_profit_factor | 1.2199 |
| gross_win_rate | 0.5538 |
| sharpe_ratio | 0.2888 |
| sortino_ratio | 0.0756 |
| max_drawdown | 0.2219 |
| cagr | 0.0267 |
| net_avg_win | 100.6358 |
| net_avg_loss | -120.2116 |
| avg_hold_time_bars | 49.6062 |
| exposure | 0.7328 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
