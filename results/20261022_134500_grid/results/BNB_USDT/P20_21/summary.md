# EMA Hourly Continuation — BNB/USDT P20_21

**Symbol:** BNB/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1195 |
| net_profit_factor | 0.0438 |
| net_win_rate | 0.1824 |
| gross_profit_factor | 0.3500 |
| gross_win_rate | 0.3314 |
| sharpe_ratio | -23.0050 |
| sortino_ratio | -14.4360 |
| max_drawdown | 1.0000 |
| cagr | -0.9996 |
| net_avg_win | 2.0989 |
| net_avg_loss | -10.7037 |
| avg_hold_time_bars | 1.6812 |
| exposure | 0.0913 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
