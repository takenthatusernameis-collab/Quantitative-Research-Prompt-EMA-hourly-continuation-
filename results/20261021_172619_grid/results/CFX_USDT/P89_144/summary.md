# EMA Hourly Continuation — CFX/USDT P89_144

**Symbol:** CFX/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 266 |
| net_profit_factor | 0.8633 |
| net_win_rate | 0.5338 |
| gross_profit_factor | 1.1446 |
| gross_win_rate | 0.5338 |
| sharpe_ratio | -0.7460 |
| sortino_ratio | -0.1759 |
| max_drawdown | 0.2293 |
| cagr | -0.0791 |
| net_avg_win | 83.0970 |
| net_avg_loss | -110.2258 |
| avg_hold_time_bars | 8.2594 |
| exposure | 0.0999 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
