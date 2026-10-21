# EMA Hourly Continuation — WOO/USDT P21_26

**Symbol:** WOO/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 257 |
| net_profit_factor | 0.5721 |
| net_win_rate | 0.4436 |
| gross_profit_factor | 0.8213 |
| gross_win_rate | 0.4436 |
| sharpe_ratio | -2.9900 |
| sortino_ratio | -0.6839 |
| max_drawdown | 0.5940 |
| cagr | -0.2709 |
| net_avg_win | 64.2537 |
| net_avg_loss | -89.5287 |
| avg_hold_time_bars | 4.2763 |
| exposure | 0.0500 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
