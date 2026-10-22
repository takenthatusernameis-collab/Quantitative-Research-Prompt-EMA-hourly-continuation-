# EMA Hourly Continuation — TRAC/USDT P21_200

**Symbol:** TRAC/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 407 |
| net_profit_factor | 0.6444 |
| net_win_rate | 0.4570 |
| gross_profit_factor | 0.8731 |
| gross_win_rate | 0.4619 |
| sharpe_ratio | -2.9130 |
| sortino_ratio | -0.8266 |
| max_drawdown | 0.6378 |
| cagr | -0.3221 |
| net_avg_win | 60.7261 |
| net_avg_loss | -79.3125 |
| avg_hold_time_bars | 33.2211 |
| exposure | 0.6146 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
