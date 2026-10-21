# EMA Hourly Continuation — AVAX/USDT P89_200

**Symbol:** AVAX/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 248 |
| net_profit_factor | 0.6419 |
| net_win_rate | 0.4597 |
| gross_profit_factor | 0.8344 |
| gross_win_rate | 0.4597 |
| sharpe_ratio | -2.1203 |
| sortino_ratio | -0.4753 |
| max_drawdown | 0.4425 |
| cagr | -0.1956 |
| net_avg_win | 66.2202 |
| net_avg_loss | -87.7592 |
| avg_hold_time_bars | 14.5645 |
| exposure | 0.1642 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
