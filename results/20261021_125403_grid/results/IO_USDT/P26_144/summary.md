# EMA Hourly Continuation — IO/USDT P26_144

**Symbol:** IO/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 371 |
| net_profit_factor | 0.8526 |
| net_win_rate | 0.5013 |
| gross_profit_factor | 0.9943 |
| gross_win_rate | 0.5013 |
| sharpe_ratio | -0.9243 |
| sortino_ratio | -0.2632 |
| max_drawdown | 0.2773 |
| cagr | -0.1167 |
| net_avg_win | 78.8702 |
| net_avg_loss | -93.0050 |
| avg_hold_time_bars | 23.9245 |
| exposure | 0.4297 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
