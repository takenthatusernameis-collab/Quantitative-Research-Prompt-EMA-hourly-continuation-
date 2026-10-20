# EMA Hourly Continuation — WEMIX/USDT P8_55

**Symbol:** WEMIX/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1532 |
| net_profit_factor | 0.2574 |
| net_win_rate | 0.3042 |
| gross_profit_factor | 0.4605 |
| gross_win_rate | 0.3211 |
| sharpe_ratio | -16.1226 |
| sortino_ratio | -8.9706 |
| max_drawdown | 1.0000 |
| cagr | -0.9899 |
| net_avg_win | 7.4385 |
| net_avg_loss | -12.6325 |
| avg_hold_time_bars | 7.1390 |
| exposure | 0.4971 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
