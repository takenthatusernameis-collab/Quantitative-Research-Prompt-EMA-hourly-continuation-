# EMA Hourly Continuation — PUNDIX/USDT P34_200

**Symbol:** PUNDIX/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 327 |
| net_profit_factor | 0.8502 |
| net_win_rate | 0.5168 |
| gross_profit_factor | 1.0849 |
| gross_win_rate | 0.5168 |
| sharpe_ratio | -0.9900 |
| sortino_ratio | -0.2566 |
| max_drawdown | 0.3490 |
| cagr | -0.1140 |
| net_avg_win | 87.9986 |
| net_avg_loss | -110.7131 |
| avg_hold_time_bars | 33.3303 |
| exposure | 0.4954 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
