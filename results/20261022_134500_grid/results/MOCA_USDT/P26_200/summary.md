# EMA Hourly Continuation — MOCA/USDT P26_200

**Symbol:** MOCA/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 346 |
| net_profit_factor | 0.5715 |
| net_win_rate | 0.4509 |
| gross_profit_factor | 0.8439 |
| gross_win_rate | 0.4595 |
| sharpe_ratio | -3.4883 |
| sortino_ratio | -0.9504 |
| max_drawdown | 0.6560 |
| cagr | -0.3709 |
| net_avg_win | 55.7425 |
| net_avg_loss | -80.0783 |
| avg_hold_time_bars | 33.6243 |
| exposure | 0.5832 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
