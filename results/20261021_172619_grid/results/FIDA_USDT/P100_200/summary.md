# EMA Hourly Continuation — FIDA/USDT P100_200

**Symbol:** FIDA/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 309 |
| net_profit_factor | 0.6884 |
| net_win_rate | 0.4725 |
| gross_profit_factor | 0.8882 |
| gross_win_rate | 0.4725 |
| sharpe_ratio | -2.0110 |
| sortino_ratio | -0.5025 |
| max_drawdown | 0.4518 |
| cagr | -0.2069 |
| net_avg_win | 66.9774 |
| net_avg_loss | -87.1504 |
| avg_hold_time_bars | 12.9159 |
| exposure | 0.1806 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
