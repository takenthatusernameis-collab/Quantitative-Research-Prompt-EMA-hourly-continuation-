# EMA Hourly Continuation — PUNDIX/USDT P26_100

**Symbol:** PUNDIX/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 512 |
| net_profit_factor | 0.6997 |
| net_win_rate | 0.4844 |
| gross_profit_factor | 0.9427 |
| gross_win_rate | 0.4863 |
| sharpe_ratio | -2.5368 |
| sortino_ratio | -0.8202 |
| max_drawdown | 0.6238 |
| cagr | -0.3133 |
| net_avg_win | 57.3995 |
| net_avg_loss | -77.0616 |
| avg_hold_time_bars | 15.8242 |
| exposure | 0.3683 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
