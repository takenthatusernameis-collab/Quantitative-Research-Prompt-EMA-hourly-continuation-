# EMA Hourly Continuation — CSPR/USDT P50_100

**Symbol:** CSPR/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 373 |
| net_profit_factor | 0.6934 |
| net_win_rate | 0.4745 |
| gross_profit_factor | 0.9004 |
| gross_win_rate | 0.4745 |
| sharpe_ratio | -2.1830 |
| sortino_ratio | -0.6017 |
| max_drawdown | 0.5051 |
| cagr | -0.2417 |
| net_avg_win | 63.9928 |
| net_avg_loss | -83.3397 |
| avg_hold_time_bars | 7.6408 |
| exposure | 0.1295 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
