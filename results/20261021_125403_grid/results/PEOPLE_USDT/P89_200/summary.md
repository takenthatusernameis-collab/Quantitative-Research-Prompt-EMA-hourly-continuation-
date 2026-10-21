# EMA Hourly Continuation — PEOPLE/USDT P89_200

**Symbol:** PEOPLE/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 292 |
| net_profit_factor | 0.8279 |
| net_win_rate | 0.5103 |
| gross_profit_factor | 1.0246 |
| gross_win_rate | 0.5103 |
| sharpe_ratio | -0.9195 |
| sortino_ratio | -0.2250 |
| max_drawdown | 0.3370 |
| cagr | -0.0995 |
| net_avg_win | 75.0471 |
| net_avg_loss | -94.4462 |
| avg_hold_time_bars | 15.4247 |
| exposure | 0.2038 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
