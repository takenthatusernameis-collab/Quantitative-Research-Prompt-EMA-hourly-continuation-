# EMA Hourly Continuation — FLR/USDT P8_26

**Symbol:** FLR/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1813 |
| net_profit_factor | 0.3645 |
| net_win_rate | 0.4076 |
| gross_profit_factor | 0.8185 |
| gross_win_rate | 0.4357 |
| sharpe_ratio | -14.2612 |
| sortino_ratio | -8.5889 |
| max_drawdown | 1.0000 |
| cagr | -0.9881 |
| net_avg_win | 7.7597 |
| net_avg_loss | -14.6501 |
| avg_hold_time_bars | 3.3574 |
| exposure | 0.2767 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
