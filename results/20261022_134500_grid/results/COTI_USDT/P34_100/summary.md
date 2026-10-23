# EMA Hourly Continuation — COTI/USDT P34_100

**Symbol:** COTI/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 688 |
| net_profit_factor | 0.6234 |
| net_win_rate | 0.4869 |
| gross_profit_factor | 0.9438 |
| gross_win_rate | 0.4942 |
| sharpe_ratio | -3.6174 |
| sortino_ratio | -1.3326 |
| max_drawdown | 0.8052 |
| cagr | -0.4734 |
| net_avg_win | 39.5340 |
| net_avg_loss | -60.1876 |
| avg_hold_time_bars | 8.4927 |
| exposure | 0.2656 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
