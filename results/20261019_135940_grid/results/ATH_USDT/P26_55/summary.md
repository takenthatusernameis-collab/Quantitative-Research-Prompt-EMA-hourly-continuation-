# EMA Hourly Continuation — ATH/USDT P26_55

**Symbol:** ATH/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 861 |
| net_profit_factor | 0.5139 |
| net_win_rate | 0.4715 |
| gross_profit_factor | 0.8875 |
| gross_win_rate | 0.4785 |
| sharpe_ratio | -5.9166 |
| sortino_ratio | -2.5253 |
| max_drawdown | 0.9473 |
| cagr | -0.7083 |
| net_avg_win | 24.6038 |
| net_avg_loss | -42.7248 |
| avg_hold_time_bars | 3.9861 |
| exposure | 0.1664 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
