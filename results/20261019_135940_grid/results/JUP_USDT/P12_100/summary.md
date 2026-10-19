# EMA Hourly Continuation — JUP/USDT P12_100

**Symbol:** JUP/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 727 |
| net_profit_factor | 0.6431 |
| net_win_rate | 0.4580 |
| gross_profit_factor | 0.9159 |
| gross_win_rate | 0.4622 |
| sharpe_ratio | -4.2362 |
| sortino_ratio | -1.6057 |
| max_drawdown | 0.8647 |
| cagr | -0.5340 |
| net_avg_win | 46.1517 |
| net_avg_loss | -60.6576 |
| avg_hold_time_bars | 16.1073 |
| exposure | 0.5323 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
