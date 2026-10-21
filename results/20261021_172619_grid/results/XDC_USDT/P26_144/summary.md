# EMA Hourly Continuation — XDC/USDT P26_144

**Symbol:** XDC/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 428 |
| net_profit_factor | 0.7195 |
| net_win_rate | 0.5023 |
| gross_profit_factor | 0.9839 |
| gross_win_rate | 0.5023 |
| sharpe_ratio | -1.9694 |
| sortino_ratio | -0.5830 |
| max_drawdown | 0.4961 |
| cagr | -0.2347 |
| net_avg_win | 58.3827 |
| net_avg_loss | -81.8998 |
| avg_hold_time_bars | 19.4182 |
| exposure | 0.3778 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
