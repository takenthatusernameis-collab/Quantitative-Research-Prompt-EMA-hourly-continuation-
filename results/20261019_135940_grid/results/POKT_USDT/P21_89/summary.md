# EMA Hourly Continuation — POKT/USDT P21_89

**Symbol:** POKT/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 898 |
| net_profit_factor | 0.5717 |
| net_win_rate | 0.4087 |
| gross_profit_factor | 0.8629 |
| gross_win_rate | 0.4131 |
| sharpe_ratio | -7.0631 |
| sortino_ratio | -2.9698 |
| max_drawdown | 0.9736 |
| cagr | -0.7593 |
| net_avg_win | 35.3672 |
| net_avg_loss | -42.7578 |
| avg_hold_time_bars | 9.4499 |
| exposure | 0.3840 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
