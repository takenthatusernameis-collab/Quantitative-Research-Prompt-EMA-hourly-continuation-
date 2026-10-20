# EMA Hourly Continuation — XEC/USDT P21_89

**Symbol:** XEC/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 812 |
| net_profit_factor | 0.5263 |
| net_win_rate | 0.4495 |
| gross_profit_factor | 0.8882 |
| gross_win_rate | 0.4631 |
| sharpe_ratio | -5.9711 |
| sortino_ratio | -2.3835 |
| max_drawdown | 0.9504 |
| cagr | -0.6879 |
| net_avg_win | 28.8311 |
| net_avg_loss | -44.7281 |
| avg_hold_time_bars | 10.4717 |
| exposure | 0.3848 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
