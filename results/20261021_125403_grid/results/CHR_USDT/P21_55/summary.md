# EMA Hourly Continuation — CHR/USDT P21_55

**Symbol:** CHR/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 569 |
| net_profit_factor | 0.7172 |
| net_win_rate | 0.4763 |
| gross_profit_factor | 0.9275 |
| gross_win_rate | 0.4763 |
| sharpe_ratio | -2.6452 |
| sortino_ratio | -0.8986 |
| max_drawdown | 0.6565 |
| cagr | -0.3376 |
| net_avg_win | 60.4605 |
| net_avg_loss | -76.6662 |
| avg_hold_time_bars | 8.1195 |
| exposure | 0.2091 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
