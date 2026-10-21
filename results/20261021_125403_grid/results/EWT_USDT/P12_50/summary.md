# EMA Hourly Continuation — EWT/USDT P12_50

**Symbol:** EWT/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 522 |
| net_profit_factor | 0.6178 |
| net_win_rate | 0.4387 |
| gross_profit_factor | 0.7878 |
| gross_win_rate | 0.4387 |
| sharpe_ratio | -3.5221 |
| sortino_ratio | -1.1404 |
| max_drawdown | 0.7317 |
| cagr | -0.4078 |
| net_avg_win | 51.6560 |
| net_avg_loss | -65.3455 |
| avg_hold_time_bars | 10.3103 |
| exposure | 0.2446 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
