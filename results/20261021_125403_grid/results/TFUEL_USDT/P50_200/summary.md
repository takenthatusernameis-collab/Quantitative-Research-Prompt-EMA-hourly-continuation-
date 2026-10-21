# EMA Hourly Continuation — TFUEL/USDT P50_200

**Symbol:** TFUEL/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 378 |
| net_profit_factor | 0.5631 |
| net_win_rate | 0.4074 |
| gross_profit_factor | 0.7148 |
| gross_win_rate | 0.4074 |
| sharpe_ratio | -3.7606 |
| sortino_ratio | -1.0295 |
| max_drawdown | 0.7067 |
| cagr | -0.3800 |
| net_avg_win | 58.6253 |
| net_avg_loss | -71.5820 |
| avg_hold_time_bars | 19.7434 |
| exposure | 0.3377 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
