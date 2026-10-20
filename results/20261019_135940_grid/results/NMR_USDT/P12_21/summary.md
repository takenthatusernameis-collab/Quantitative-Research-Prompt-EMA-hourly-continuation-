# EMA Hourly Continuation — NMR/USDT P12_21

**Symbol:** NMR/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1505 |
| net_profit_factor | 0.3325 |
| net_win_rate | 0.4013 |
| gross_profit_factor | 0.8392 |
| gross_win_rate | 0.4498 |
| sharpe_ratio | -13.6364 |
| sortino_ratio | -7.5471 |
| max_drawdown | 0.9999 |
| cagr | -0.9801 |
| net_avg_win | 8.2464 |
| net_avg_loss | -16.6263 |
| avg_hold_time_bars | 2.5581 |
| exposure | 0.1750 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
