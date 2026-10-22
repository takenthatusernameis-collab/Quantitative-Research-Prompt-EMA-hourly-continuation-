# EMA Hourly Continuation — CFX/USDT P89_144

**Symbol:** CFX/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 469 |
| net_profit_factor | 0.5669 |
| net_win_rate | 0.4904 |
| gross_profit_factor | 0.9719 |
| gross_win_rate | 0.4947 |
| sharpe_ratio | -3.7467 |
| sortino_ratio | -1.1337 |
| max_drawdown | 0.7586 |
| cagr | -0.4284 |
| net_avg_win | 42.9431 |
| net_avg_loss | -72.8979 |
| avg_hold_time_bars | 5.4776 |
| exposure | 0.1168 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
