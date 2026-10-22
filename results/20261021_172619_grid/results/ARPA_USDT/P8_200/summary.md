# EMA Hourly Continuation — ARPA/USDT P8_200

**Symbol:** ARPA/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 399 |
| net_profit_factor | 0.6401 |
| net_win_rate | 0.4511 |
| gross_profit_factor | 0.7998 |
| gross_win_rate | 0.4511 |
| sharpe_ratio | -2.6856 |
| sortino_ratio | -0.7578 |
| max_drawdown | 0.6050 |
| cagr | -0.2963 |
| net_avg_win | 58.0786 |
| net_avg_loss | -74.5777 |
| avg_hold_time_bars | 41.1880 |
| exposure | 0.7437 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
