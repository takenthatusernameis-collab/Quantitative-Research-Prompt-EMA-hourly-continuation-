# EMA Hourly Continuation — FIL/USDT P20_100

**Symbol:** FIL/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 679 |
| net_profit_factor | 0.5241 |
| net_win_rate | 0.4389 |
| gross_profit_factor | 0.8225 |
| gross_win_rate | 0.4433 |
| sharpe_ratio | -5.5182 |
| sortino_ratio | -2.0186 |
| max_drawdown | 0.9202 |
| cagr | -0.6230 |
| net_avg_win | 33.7658 |
| net_avg_loss | -50.3915 |
| avg_hold_time_bars | 12.7879 |
| exposure | 0.3947 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
