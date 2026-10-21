# EMA Hourly Continuation — TIA/USDT P26_100

**Symbol:** TIA/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 419 |
| net_profit_factor | 0.8831 |
| net_win_rate | 0.5131 |
| gross_profit_factor | 1.0545 |
| gross_win_rate | 0.5131 |
| sharpe_ratio | -0.8184 |
| sortino_ratio | -0.2406 |
| max_drawdown | 0.3408 |
| cagr | -0.1080 |
| net_avg_win | 87.6811 |
| net_avg_loss | -104.6401 |
| avg_hold_time_bars | 18.3174 |
| exposure | 0.3489 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
