# EMA Hourly Continuation — ONT/USDT P55_89

**Symbol:** ONT/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 670 |
| net_profit_factor | 0.4522 |
| net_win_rate | 0.4522 |
| gross_profit_factor | 0.8037 |
| gross_win_rate | 0.4582 |
| sharpe_ratio | -5.9383 |
| sortino_ratio | -2.1800 |
| max_drawdown | 0.9296 |
| cagr | -0.6469 |
| net_avg_win | 25.2700 |
| net_avg_loss | -46.1396 |
| avg_hold_time_bars | 4.7194 |
| exposure | 0.1431 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
