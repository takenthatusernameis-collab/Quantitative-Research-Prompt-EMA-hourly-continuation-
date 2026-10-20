# EMA Hourly Continuation — WAVES/USDT P26_34

**Symbol:** WAVES/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1195 |
| net_profit_factor | 0.2112 |
| net_win_rate | 0.3197 |
| gross_profit_factor | 0.7410 |
| gross_win_rate | 0.3950 |
| sharpe_ratio | -16.0734 |
| sortino_ratio | -8.2290 |
| max_drawdown | 1.0000 |
| cagr | -0.9883 |
| net_avg_win | 7.0089 |
| net_avg_loss | -15.5932 |
| avg_hold_time_bars | 2.1933 |
| exposure | 0.1191 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
