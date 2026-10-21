# EMA Hourly Continuation — AMP/USDT P12_200

**Symbol:** AMP/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 460 |
| net_profit_factor | 0.6325 |
| net_win_rate | 0.4391 |
| gross_profit_factor | 0.7814 |
| gross_win_rate | 0.4391 |
| sharpe_ratio | -3.0288 |
| sortino_ratio | -0.9187 |
| max_drawdown | 0.6635 |
| cagr | -0.3453 |
| net_avg_win | 55.7891 |
| net_avg_loss | -69.0592 |
| avg_hold_time_bars | 31.3674 |
| exposure | 0.6559 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
