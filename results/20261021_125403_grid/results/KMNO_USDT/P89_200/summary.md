# EMA Hourly Continuation — KMNO/USDT P89_200

**Symbol:** KMNO/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 272 |
| net_profit_factor | 0.7056 |
| net_win_rate | 0.4743 |
| gross_profit_factor | 0.8942 |
| gross_win_rate | 0.4743 |
| sharpe_ratio | -1.8339 |
| sortino_ratio | -0.4329 |
| max_drawdown | 0.4080 |
| cagr | -0.1820 |
| net_avg_win | 72.7272 |
| net_avg_loss | -92.9761 |
| avg_hold_time_bars | 16.3824 |
| exposure | 0.2057 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
