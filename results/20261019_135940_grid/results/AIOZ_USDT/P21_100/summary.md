# EMA Hourly Continuation — AIOZ/USDT P21_100

**Symbol:** AIOZ/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 687 |
| net_profit_factor | 0.6837 |
| net_win_rate | 0.4876 |
| gross_profit_factor | 0.9741 |
| gross_win_rate | 0.4920 |
| sharpe_ratio | -3.5630 |
| sortino_ratio | -1.3179 |
| max_drawdown | 0.8097 |
| cagr | -0.4672 |
| net_avg_win | 51.2560 |
| net_avg_loss | -71.3443 |
| avg_hold_time_bars | 13.3435 |
| exposure | 0.4167 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
