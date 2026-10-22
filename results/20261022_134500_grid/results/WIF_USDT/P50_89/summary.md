# EMA Hourly Continuation — WIF/USDT P50_89

**Symbol:** WIF/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 669 |
| net_profit_factor | 0.6184 |
| net_win_rate | 0.4873 |
| gross_profit_factor | 0.9888 |
| gross_win_rate | 0.4963 |
| sharpe_ratio | -4.2041 |
| sortino_ratio | -1.5332 |
| max_drawdown | 0.8476 |
| cagr | -0.5223 |
| net_avg_win | 41.9326 |
| net_avg_loss | -64.4491 |
| avg_hold_time_bars | 4.5770 |
| exposure | 0.1392 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
