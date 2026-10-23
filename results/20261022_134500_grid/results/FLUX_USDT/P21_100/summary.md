# EMA Hourly Continuation — FLUX/USDT P21_100

**Symbol:** FLUX/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 690 |
| net_profit_factor | 0.6342 |
| net_win_rate | 0.4884 |
| gross_profit_factor | 0.9958 |
| gross_win_rate | 0.4942 |
| sharpe_ratio | -3.7512 |
| sortino_ratio | -1.3891 |
| max_drawdown | 0.8200 |
| cagr | -0.4849 |
| net_avg_win | 41.7173 |
| net_avg_loss | -62.8003 |
| avg_hold_time_bars | 13.1232 |
| exposure | 0.4116 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
