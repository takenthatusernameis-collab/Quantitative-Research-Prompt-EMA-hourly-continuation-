# EMA Hourly Continuation — SWFTC/USDT P8_200

**Symbol:** SWFTC/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 418 |
| net_profit_factor | 0.7686 |
| net_win_rate | 0.4737 |
| gross_profit_factor | 0.9196 |
| gross_win_rate | 0.4737 |
| sharpe_ratio | -1.9072 |
| sortino_ratio | -0.5542 |
| max_drawdown | 0.5292 |
| cagr | -0.2259 |
| net_avg_win | 79.5697 |
| net_avg_loss | -93.1722 |
| avg_hold_time_bars | 35.9928 |
| exposure | 0.6839 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
