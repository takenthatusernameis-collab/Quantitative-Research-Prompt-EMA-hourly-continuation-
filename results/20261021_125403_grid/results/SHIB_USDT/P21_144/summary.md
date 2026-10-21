# EMA Hourly Continuation — SHIB/USDT P21_144

**Symbol:** SHIB/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 388 |
| net_profit_factor | 0.8915 |
| net_win_rate | 0.5284 |
| gross_profit_factor | 1.1294 |
| gross_win_rate | 0.5284 |
| sharpe_ratio | -0.7329 |
| sortino_ratio | -0.2082 |
| max_drawdown | 0.3025 |
| cagr | -0.0938 |
| net_avg_win | 87.8153 |
| net_avg_loss | -110.3496 |
| avg_hold_time_bars | 25.5773 |
| exposure | 0.4511 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
