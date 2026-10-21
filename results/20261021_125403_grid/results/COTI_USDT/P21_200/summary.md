# EMA Hourly Continuation — COTI/USDT P21_200

**Symbol:** COTI/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 328 |
| net_profit_factor | 0.8846 |
| net_win_rate | 0.5091 |
| gross_profit_factor | 1.0338 |
| gross_win_rate | 0.5091 |
| sharpe_ratio | -0.6774 |
| sortino_ratio | -0.1760 |
| max_drawdown | 0.3016 |
| cagr | -0.0807 |
| net_avg_win | 87.4071 |
| net_avg_loss | -102.4919 |
| avg_hold_time_bars | 40.6006 |
| exposure | 0.6053 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
