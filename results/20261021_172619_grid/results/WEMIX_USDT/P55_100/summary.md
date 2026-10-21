# EMA Hourly Continuation — WEMIX/USDT P55_100

**Symbol:** WEMIX/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 283 |
| net_profit_factor | 0.5213 |
| net_win_rate | 0.4064 |
| gross_profit_factor | 0.6909 |
| gross_win_rate | 0.4064 |
| sharpe_ratio | -3.4891 |
| sortino_ratio | -0.8315 |
| max_drawdown | 0.6186 |
| cagr | -0.3187 |
| net_avg_win | 58.5780 |
| net_avg_loss | -76.9175 |
| avg_hold_time_bars | 10.8410 |
| exposure | 0.1395 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
