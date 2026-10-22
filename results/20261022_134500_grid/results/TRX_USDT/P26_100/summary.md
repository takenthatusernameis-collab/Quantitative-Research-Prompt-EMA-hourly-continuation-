# EMA Hourly Continuation — TRX/USDT P26_100

**Symbol:** TRX/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 601 |
| net_profit_factor | 0.3322 |
| net_win_rate | 0.3977 |
| gross_profit_factor | 1.0699 |
| gross_win_rate | 0.4958 |
| sharpe_ratio | -9.0085 |
| sortino_ratio | -3.1699 |
| max_drawdown | 0.9855 |
| cagr | -0.8139 |
| net_avg_win | 20.5060 |
| net_avg_loss | -40.7579 |
| avg_hold_time_bars | 11.4609 |
| exposure | 0.3131 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
