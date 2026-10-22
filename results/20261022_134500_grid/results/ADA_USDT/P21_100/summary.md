# EMA Hourly Continuation — ADA/USDT P21_100

**Symbol:** ADA/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 679 |
| net_profit_factor | 0.5372 |
| net_win_rate | 0.4639 |
| gross_profit_factor | 0.8714 |
| gross_win_rate | 0.4742 |
| sharpe_ratio | -4.7623 |
| sortino_ratio | -1.7375 |
| max_drawdown | 0.8858 |
| cagr | -0.5713 |
| net_avg_win | 32.4610 |
| net_avg_loss | -52.2894 |
| avg_hold_time_bars | 12.3196 |
| exposure | 0.3802 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
