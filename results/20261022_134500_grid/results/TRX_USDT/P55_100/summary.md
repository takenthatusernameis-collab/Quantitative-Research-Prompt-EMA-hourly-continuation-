# EMA Hourly Continuation — TRX/USDT P55_100

**Symbol:** TRX/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 537 |
| net_profit_factor | 0.2409 |
| net_win_rate | 0.3557 |
| gross_profit_factor | 1.0367 |
| gross_win_rate | 0.5047 |
| sharpe_ratio | -9.7440 |
| sortino_ratio | -3.3597 |
| max_drawdown | 0.9883 |
| cagr | -0.8299 |
| net_avg_win | 16.4178 |
| net_avg_loss | -37.6266 |
| avg_hold_time_bars | 5.9143 |
| exposure | 0.1444 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
