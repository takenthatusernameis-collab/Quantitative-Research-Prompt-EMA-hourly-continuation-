# EMA Hourly Continuation — PYTH/USDT P144_200

**Symbol:** PYTH/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 412 |
| net_profit_factor | 0.5153 |
| net_win_rate | 0.4515 |
| gross_profit_factor | 0.8623 |
| gross_win_rate | 0.4612 |
| sharpe_ratio | -4.2082 |
| sortino_ratio | -1.1987 |
| max_drawdown | 0.7856 |
| cagr | -0.4452 |
| net_avg_win | 44.1455 |
| net_avg_loss | -70.5040 |
| avg_hold_time_bars | 4.9490 |
| exposure | 0.0927 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
