# EMA Hourly Continuation — PYTH/USDT P12_100

**Symbol:** PYTH/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 465 |
| net_profit_factor | 0.8311 |
| net_win_rate | 0.4946 |
| gross_profit_factor | 0.9742 |
| gross_win_rate | 0.4946 |
| sharpe_ratio | -1.2467 |
| sortino_ratio | -0.3839 |
| max_drawdown | 0.4225 |
| cagr | -0.1641 |
| net_avg_win | 77.5469 |
| net_avg_loss | -91.3212 |
| avg_hold_time_bars | 25.2925 |
| exposure | 0.5346 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
