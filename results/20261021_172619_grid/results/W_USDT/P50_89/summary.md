# EMA Hourly Continuation — W/USDT P50_89

**Symbol:** W/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 343 |
| net_profit_factor | 0.7949 |
| net_win_rate | 0.5131 |
| gross_profit_factor | 1.0252 |
| gross_win_rate | 0.5131 |
| sharpe_ratio | -1.2113 |
| sortino_ratio | -0.3222 |
| max_drawdown | 0.3723 |
| cagr | -0.1384 |
| net_avg_win | 68.7354 |
| net_avg_loss | -91.1256 |
| avg_hold_time_bars | 7.2157 |
| exposure | 0.1125 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
