# EMA Hourly Continuation — ZETA/USDT P89_100

**Symbol:** ZETA/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 645 |
| net_profit_factor | 0.3942 |
| net_win_rate | 0.3907 |
| gross_profit_factor | 0.9577 |
| gross_win_rate | 0.4403 |
| sharpe_ratio | -9.0485 |
| sortino_ratio | -3.3050 |
| max_drawdown | 0.9863 |
| cagr | -0.8153 |
| net_avg_win | 25.4544 |
| net_avg_loss | -41.4083 |
| avg_hold_time_bars | 2.4310 |
| exposure | 0.0710 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
