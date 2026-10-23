# EMA Hourly Continuation — BLUR/USDT P55_100

**Symbol:** BLUR/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 606 |
| net_profit_factor | 0.6023 |
| net_win_rate | 0.4752 |
| gross_profit_factor | 1.0146 |
| gross_win_rate | 0.4901 |
| sharpe_ratio | -4.3597 |
| sortino_ratio | -1.5207 |
| max_drawdown | 0.8451 |
| cagr | -0.5138 |
| net_avg_win | 44.0641 |
| net_avg_loss | -66.2538 |
| avg_hold_time_bars | 5.4917 |
| exposure | 0.1506 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
