# EMA Hourly Continuation — FET/USDT P12_200

**Symbol:** FET/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 300 |
| net_profit_factor | 0.7531 |
| net_win_rate | 0.4900 |
| gross_profit_factor | 0.9598 |
| gross_win_rate | 0.4933 |
| sharpe_ratio | -1.4621 |
| sortino_ratio | -0.3588 |
| max_drawdown | 0.4263 |
| cagr | -0.1565 |
| net_avg_win | 72.1648 |
| net_avg_loss | -92.0697 |
| avg_hold_time_bars | 58.5867 |
| exposure | 0.7989 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
