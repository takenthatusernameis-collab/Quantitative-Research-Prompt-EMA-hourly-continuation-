# EMA Hourly Continuation — BAND/USDT P89_200

**Symbol:** BAND/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 392 |
| net_profit_factor | 0.6219 |
| net_win_rate | 0.4847 |
| gross_profit_factor | 0.9469 |
| gross_win_rate | 0.4949 |
| sharpe_ratio | -2.7949 |
| sortino_ratio | -0.7849 |
| max_drawdown | 0.6147 |
| cagr | -0.3069 |
| net_avg_win | 52.2425 |
| net_avg_loss | -79.0112 |
| avg_hold_time_bars | 10.6046 |
| exposure | 0.1881 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
