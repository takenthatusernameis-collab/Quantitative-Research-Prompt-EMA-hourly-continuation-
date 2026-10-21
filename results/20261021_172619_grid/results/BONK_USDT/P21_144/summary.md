# EMA Hourly Continuation — BONK/USDT P21_144

**Symbol:** BONK/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 344 |
| net_profit_factor | 0.8544 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9905 |
| gross_win_rate | 0.5029 |
| sharpe_ratio | -0.8602 |
| sortino_ratio | -0.2282 |
| max_drawdown | 0.3887 |
| cagr | -0.1024 |
| net_avg_win | 81.0965 |
| net_avg_loss | -94.9138 |
| avg_hold_time_bars | 35.6890 |
| exposure | 0.5580 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
