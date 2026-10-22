# EMA Hourly Continuation — GMT/USDT P100_200

**Symbol:** GMT/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 278 |
| net_profit_factor | 0.7574 |
| net_win_rate | 0.4964 |
| gross_profit_factor | 0.9625 |
| gross_win_rate | 0.4964 |
| sharpe_ratio | -1.3599 |
| sortino_ratio | -0.3242 |
| max_drawdown | 0.3466 |
| cagr | -0.1389 |
| net_avg_win | 70.8244 |
| net_avg_loss | -92.1784 |
| avg_hold_time_bars | 12.0468 |
| exposure | 0.1522 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
