# EMA Hourly Continuation — ONDO/USDT P34_144

**Symbol:** ONDO/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 369 |
| net_profit_factor | 0.7765 |
| net_win_rate | 0.4770 |
| gross_profit_factor | 0.9249 |
| gross_win_rate | 0.4770 |
| sharpe_ratio | -1.6141 |
| sortino_ratio | -0.4416 |
| max_drawdown | 0.4845 |
| cagr | -0.1839 |
| net_avg_win | 78.9065 |
| net_avg_loss | -92.6635 |
| avg_hold_time_bars | 18.9404 |
| exposure | 0.3177 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
