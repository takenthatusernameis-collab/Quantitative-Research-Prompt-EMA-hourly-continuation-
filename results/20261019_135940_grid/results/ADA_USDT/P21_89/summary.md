# EMA Hourly Continuation — ADA/USDT P21_89

**Symbol:** ADA/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 727 |
| net_profit_factor | 0.5250 |
| net_win_rate | 0.4663 |
| gross_profit_factor | 0.8813 |
| gross_win_rate | 0.4787 |
| sharpe_ratio | -4.9221 |
| sortino_ratio | -1.8740 |
| max_drawdown | 0.8997 |
| cagr | -0.5923 |
| net_avg_win | 29.1721 |
| net_avg_loss | -48.5531 |
| avg_hold_time_bars | 10.4691 |
| exposure | 0.3460 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
