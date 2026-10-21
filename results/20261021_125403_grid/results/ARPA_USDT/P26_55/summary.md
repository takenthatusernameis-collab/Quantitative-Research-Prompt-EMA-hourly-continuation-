# EMA Hourly Continuation — ARPA/USDT P26_55

**Symbol:** ARPA/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 548 |
| net_profit_factor | 0.6577 |
| net_win_rate | 0.4745 |
| gross_profit_factor | 0.9462 |
| gross_win_rate | 0.4781 |
| sharpe_ratio | -3.4793 |
| sortino_ratio | -1.1637 |
| max_drawdown | 0.7513 |
| cagr | -0.4131 |
| net_avg_win | 54.6412 |
| net_avg_loss | -74.9976 |
| avg_hold_time_bars | 7.4872 |
| exposure | 0.1857 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
