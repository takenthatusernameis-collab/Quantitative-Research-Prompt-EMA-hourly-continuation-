# EMA Hourly Continuation — AVA/USDT P34_200

**Symbol:** AVA/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 325 |
| net_profit_factor | 0.8734 |
| net_win_rate | 0.5200 |
| gross_profit_factor | 1.0629 |
| gross_win_rate | 0.5200 |
| sharpe_ratio | -0.6458 |
| sortino_ratio | -0.1676 |
| max_drawdown | 0.3251 |
| cagr | -0.0770 |
| net_avg_win | 74.3279 |
| net_avg_loss | -92.1987 |
| avg_hold_time_bars | 31.6277 |
| exposure | 0.4672 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
