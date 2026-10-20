# EMA Hourly Continuation — POPCAT/USDT P34_144

**Symbol:** POPCAT/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 442 |
| net_profit_factor | 0.6864 |
| net_win_rate | 0.4683 |
| gross_profit_factor | 0.9013 |
| gross_win_rate | 0.4751 |
| sharpe_ratio | -2.8131 |
| sortino_ratio | -0.9000 |
| max_drawdown | 0.6100 |
| cagr | -0.3456 |
| net_avg_win | 63.4282 |
| net_avg_loss | -81.4009 |
| avg_hold_time_bars | 17.6719 |
| exposure | 0.4126 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
