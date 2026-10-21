# EMA Hourly Continuation — PUNDIX/USDT P26_200

**Symbol:** PUNDIX/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 341 |
| net_profit_factor | 0.8072 |
| net_win_rate | 0.5044 |
| gross_profit_factor | 1.0381 |
| gross_win_rate | 0.5044 |
| sharpe_ratio | -1.3518 |
| sortino_ratio | -0.3568 |
| max_drawdown | 0.3751 |
| cagr | -0.1534 |
| net_avg_win | 83.2156 |
| net_avg_loss | -104.9170 |
| avg_hold_time_bars | 37.1789 |
| exposure | 0.5763 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
