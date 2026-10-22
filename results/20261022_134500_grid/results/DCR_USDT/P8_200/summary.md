# EMA Hourly Continuation — DCR/USDT P8_200

**Symbol:** DCR/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 522 |
| net_profit_factor | 0.6906 |
| net_win_rate | 0.4847 |
| gross_profit_factor | 0.9538 |
| gross_win_rate | 0.4904 |
| sharpe_ratio | -2.5973 |
| sortino_ratio | -0.8363 |
| max_drawdown | 0.6468 |
| cagr | -0.3251 |
| net_avg_win | 55.5205 |
| net_avg_loss | -75.6078 |
| avg_hold_time_bars | 31.3908 |
| exposure | 0.7415 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
