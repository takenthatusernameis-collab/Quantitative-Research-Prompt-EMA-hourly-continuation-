# EMA Hourly Continuation — AGLD/USDT P50_55

**Symbol:** AGLD/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 831 |
| net_profit_factor | 0.1951 |
| net_win_rate | 0.3418 |
| gross_profit_factor | 0.6267 |
| gross_win_rate | 0.4031 |
| sharpe_ratio | -11.8032 |
| sortino_ratio | -4.9209 |
| max_drawdown | 0.9985 |
| cagr | -0.9236 |
| net_avg_win | 8.5199 |
| net_avg_loss | -22.6772 |
| avg_hold_time_bars | 2.5307 |
| exposure | 0.0952 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
