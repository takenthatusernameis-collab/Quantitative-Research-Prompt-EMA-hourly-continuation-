# EMA Hourly Continuation — DEGEN/USDT P20_200

**Symbol:** DEGEN/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 412 |
| net_profit_factor | 0.7514 |
| net_win_rate | 0.4830 |
| gross_profit_factor | 0.9721 |
| gross_win_rate | 0.4903 |
| sharpe_ratio | -1.9766 |
| sortino_ratio | -0.5676 |
| max_drawdown | 0.5119 |
| cagr | -0.2364 |
| net_avg_win | 74.6605 |
| net_avg_loss | -92.8251 |
| avg_hold_time_bars | 33.3301 |
| exposure | 0.6252 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
