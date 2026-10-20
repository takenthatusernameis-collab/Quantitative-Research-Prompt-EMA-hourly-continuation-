# EMA Hourly Continuation — FIDA/USDT P50_200

**Symbol:** FIDA/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 437 |
| net_profit_factor | 0.5732 |
| net_win_rate | 0.4600 |
| gross_profit_factor | 0.8427 |
| gross_win_rate | 0.4622 |
| sharpe_ratio | -3.3537 |
| sortino_ratio | -0.9800 |
| max_drawdown | 0.7062 |
| cagr | -0.3773 |
| net_avg_win | 46.5871 |
| net_avg_loss | -69.2230 |
| avg_hold_time_bars | 19.1121 |
| exposure | 0.3779 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
