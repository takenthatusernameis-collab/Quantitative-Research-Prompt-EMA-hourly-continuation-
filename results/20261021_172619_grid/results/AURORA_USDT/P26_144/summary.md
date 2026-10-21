# EMA Hourly Continuation — AURORA/USDT P26_144

**Symbol:** AURORA/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 351 |
| net_profit_factor | 0.7204 |
| net_win_rate | 0.4815 |
| gross_profit_factor | 0.9373 |
| gross_win_rate | 0.4815 |
| sharpe_ratio | -2.0019 |
| sortino_ratio | -0.5342 |
| max_drawdown | 0.4762 |
| cagr | -0.2184 |
| net_avg_win | 70.3422 |
| net_avg_loss | -90.6680 |
| avg_hold_time_bars | 27.1738 |
| exposure | 0.4335 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
