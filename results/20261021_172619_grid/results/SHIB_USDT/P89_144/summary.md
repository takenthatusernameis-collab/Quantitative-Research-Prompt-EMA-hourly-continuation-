# EMA Hourly Continuation — SHIB/USDT P89_144

**Symbol:** SHIB/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 255 |
| net_profit_factor | 0.7019 |
| net_win_rate | 0.4980 |
| gross_profit_factor | 0.9833 |
| gross_win_rate | 0.4980 |
| sharpe_ratio | -1.7497 |
| sortino_ratio | -0.4015 |
| max_drawdown | 0.3892 |
| cagr | -0.1675 |
| net_avg_win | 68.4021 |
| net_avg_loss | -96.6962 |
| avg_hold_time_bars | 8.5451 |
| exposure | 0.0990 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
