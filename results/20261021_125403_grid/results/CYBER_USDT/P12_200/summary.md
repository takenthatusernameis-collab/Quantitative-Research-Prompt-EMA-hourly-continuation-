# EMA Hourly Continuation — CYBER/USDT P12_200

**Symbol:** CYBER/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 322 |
| net_profit_factor | 0.8631 |
| net_win_rate | 0.5031 |
| gross_profit_factor | 1.0114 |
| gross_win_rate | 0.5031 |
| sharpe_ratio | -0.8313 |
| sortino_ratio | -0.2137 |
| max_drawdown | 0.3151 |
| cagr | -0.0959 |
| net_avg_win | 87.0439 |
| net_avg_loss | -102.1108 |
| avg_hold_time_bars | 49.4503 |
| exposure | 0.7238 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
