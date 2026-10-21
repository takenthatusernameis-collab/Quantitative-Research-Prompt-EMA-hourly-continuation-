# EMA Hourly Continuation — METIS/USDT P50_200

**Symbol:** METIS/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 307 |
| net_profit_factor | 0.6507 |
| net_win_rate | 0.4365 |
| gross_profit_factor | 0.7735 |
| gross_win_rate | 0.4365 |
| sharpe_ratio | -2.3721 |
| sortino_ratio | -0.5873 |
| max_drawdown | 0.4940 |
| cagr | -0.2376 |
| net_avg_win | 68.6670 |
| net_avg_loss | -81.7424 |
| avg_hold_time_bars | 27.7655 |
| exposure | 0.3875 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
