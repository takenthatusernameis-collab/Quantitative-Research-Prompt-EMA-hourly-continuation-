# EMA Hourly Continuation — COTI/USDT P8_200

**Symbol:** COTI/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 345 |
| net_profit_factor | 0.9272 |
| net_win_rate | 0.5188 |
| gross_profit_factor | 1.0715 |
| gross_win_rate | 0.5188 |
| sharpe_ratio | -0.4297 |
| sortino_ratio | -0.1146 |
| max_drawdown | 0.3258 |
| cagr | -0.0558 |
| net_avg_win | 95.5200 |
| net_avg_loss | -111.0844 |
| avg_hold_time_bars | 49.7043 |
| exposure | 0.7795 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
