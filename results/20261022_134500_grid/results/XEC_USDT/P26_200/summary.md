# EMA Hourly Continuation — XEC/USDT P26_200

**Symbol:** XEC/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 435 |
| net_profit_factor | 0.6208 |
| net_win_rate | 0.4736 |
| gross_profit_factor | 0.9427 |
| gross_win_rate | 0.4828 |
| sharpe_ratio | -3.3166 |
| sortino_ratio | -0.9608 |
| max_drawdown | 0.7146 |
| cagr | -0.3772 |
| net_avg_win | 55.3998 |
| net_avg_loss | -80.2790 |
| avg_hold_time_bars | 29.4046 |
| exposure | 0.5788 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
