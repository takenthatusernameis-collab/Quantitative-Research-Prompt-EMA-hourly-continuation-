# EMA Hourly Continuation — CRO/USDT P34_200

**Symbol:** CRO/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 249 |
| net_profit_factor | 0.7628 |
| net_win_rate | 0.5100 |
| gross_profit_factor | 1.0048 |
| gross_win_rate | 0.5100 |
| sharpe_ratio | -1.1835 |
| sortino_ratio | -0.2679 |
| max_drawdown | 0.3429 |
| cagr | -0.1166 |
| net_avg_win | 67.7437 |
| net_avg_loss | -92.4525 |
| avg_hold_time_bars | 50.9880 |
| exposure | 0.5771 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
