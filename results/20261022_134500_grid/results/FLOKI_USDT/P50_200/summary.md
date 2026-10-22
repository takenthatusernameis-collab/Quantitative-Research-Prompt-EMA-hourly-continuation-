# EMA Hourly Continuation — FLOKI/USDT P50_200

**Symbol:** FLOKI/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 383 |
| net_profit_factor | 0.6444 |
| net_win_rate | 0.4700 |
| gross_profit_factor | 0.9047 |
| gross_win_rate | 0.4726 |
| sharpe_ratio | -2.8855 |
| sortino_ratio | -0.7880 |
| max_drawdown | 0.6385 |
| cagr | -0.3177 |
| net_avg_win | 62.1298 |
| net_avg_loss | -85.4881 |
| avg_hold_time_bars | 24.3029 |
| exposure | 0.4231 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
