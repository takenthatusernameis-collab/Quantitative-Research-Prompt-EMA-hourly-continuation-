# EMA Hourly Continuation — JST/USDT P26_200

**Symbol:** JST/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 378 |
| net_profit_factor | 0.4630 |
| net_win_rate | 0.4815 |
| gross_profit_factor | 0.9344 |
| gross_win_rate | 0.5026 |
| sharpe_ratio | -3.8501 |
| sortino_ratio | -1.0260 |
| max_drawdown | 0.7430 |
| cagr | -0.4152 |
| net_avg_win | 35.1363 |
| net_avg_loss | -70.4641 |
| avg_hold_time_bars | 30.4947 |
| exposure | 0.5216 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
