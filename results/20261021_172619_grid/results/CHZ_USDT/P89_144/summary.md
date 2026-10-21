# EMA Hourly Continuation — CHZ/USDT P89_144

**Symbol:** CHZ/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 284 |
| net_profit_factor | 0.6212 |
| net_win_rate | 0.4507 |
| gross_profit_factor | 0.8437 |
| gross_win_rate | 0.4507 |
| sharpe_ratio | -2.6567 |
| sortino_ratio | -0.6384 |
| max_drawdown | 0.5352 |
| cagr | -0.2550 |
| net_avg_win | 66.9558 |
| net_avg_loss | -88.4332 |
| avg_hold_time_bars | 6.8486 |
| exposure | 0.0884 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
