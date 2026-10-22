# EMA Hourly Continuation — TRX/USDT P26_89

**Symbol:** TRX/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 640 |
| net_profit_factor | 0.2899 |
| net_win_rate | 0.3922 |
| gross_profit_factor | 0.9506 |
| gross_win_rate | 0.4828 |
| sharpe_ratio | -9.8513 |
| sortino_ratio | -3.6062 |
| max_drawdown | 0.9926 |
| cagr | -0.8579 |
| net_avg_win | 16.1409 |
| net_avg_loss | -35.9304 |
| avg_hold_time_bars | 9.5344 |
| exposure | 0.2774 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
