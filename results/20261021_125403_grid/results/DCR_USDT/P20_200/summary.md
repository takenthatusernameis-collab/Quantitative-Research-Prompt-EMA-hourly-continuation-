# EMA Hourly Continuation — DCR/USDT P20_200

**Symbol:** DCR/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 400 |
| net_profit_factor | 0.8217 |
| net_win_rate | 0.5125 |
| gross_profit_factor | 1.0380 |
| gross_win_rate | 0.5125 |
| sharpe_ratio | -1.1467 |
| sortino_ratio | -0.3277 |
| max_drawdown | 0.3920 |
| cagr | -0.1421 |
| net_avg_win | 72.0718 |
| net_avg_loss | -92.2091 |
| avg_hold_time_bars | 31.8700 |
| exposure | 0.5769 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
