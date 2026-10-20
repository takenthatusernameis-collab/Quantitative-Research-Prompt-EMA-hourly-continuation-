# EMA Hourly Continuation — BIGTIME/USDT P55_200

**Symbol:** BIGTIME/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 345 |
| net_profit_factor | 0.8108 |
| net_win_rate | 0.5101 |
| gross_profit_factor | 1.0878 |
| gross_win_rate | 0.5159 |
| sharpe_ratio | -1.3004 |
| sortino_ratio | -0.3440 |
| max_drawdown | 0.4043 |
| cagr | -0.1484 |
| net_avg_win | 81.0807 |
| net_avg_loss | -104.1482 |
| avg_hold_time_bars | 24.7623 |
| exposure | 0.3866 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
