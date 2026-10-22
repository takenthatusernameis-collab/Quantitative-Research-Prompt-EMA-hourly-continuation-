# EMA Hourly Continuation — BICO/USDT P55_100

**Symbol:** BICO/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 435 |
| net_profit_factor | 0.7399 |
| net_win_rate | 0.4943 |
| gross_profit_factor | 0.9758 |
| gross_win_rate | 0.4943 |
| sharpe_ratio | -1.9523 |
| sortino_ratio | -0.5831 |
| max_drawdown | 0.5066 |
| cagr | -0.2352 |
| net_avg_win | 64.8490 |
| net_avg_loss | -85.6495 |
| avg_hold_time_bars | 8.7264 |
| exposure | 0.1725 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
