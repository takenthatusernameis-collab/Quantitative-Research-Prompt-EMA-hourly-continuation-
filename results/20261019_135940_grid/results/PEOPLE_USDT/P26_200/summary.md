# EMA Hourly Continuation — PEOPLE/USDT P26_200

**Symbol:** PEOPLE/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 362 |
| net_profit_factor | 0.7550 |
| net_win_rate | 0.4972 |
| gross_profit_factor | 0.9975 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.6416 |
| sortino_ratio | -0.4418 |
| max_drawdown | 0.4516 |
| cagr | -0.1876 |
| net_avg_win | 69.8533 |
| net_avg_loss | -91.4987 |
| avg_hold_time_bars | 35.4420 |
| exposure | 0.5806 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
