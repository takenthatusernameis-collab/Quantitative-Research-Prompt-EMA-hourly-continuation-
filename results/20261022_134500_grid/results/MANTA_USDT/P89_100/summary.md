# EMA Hourly Continuation — MANTA/USDT P89_100

**Symbol:** MANTA/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 605 |
| net_profit_factor | 0.2788 |
| net_win_rate | 0.4000 |
| gross_profit_factor | 0.7170 |
| gross_win_rate | 0.4298 |
| sharpe_ratio | -8.5602 |
| sortino_ratio | -3.0385 |
| max_drawdown | 0.9797 |
| cagr | -0.7872 |
| net_avg_win | 15.6433 |
| net_avg_loss | -37.4115 |
| avg_hold_time_bars | 2.4777 |
| exposure | 0.0681 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
