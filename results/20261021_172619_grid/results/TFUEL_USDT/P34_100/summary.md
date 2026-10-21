# EMA Hourly Continuation — TFUEL/USDT P34_100

**Symbol:** TFUEL/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 507 |
| net_profit_factor | 0.5118 |
| net_win_rate | 0.3886 |
| gross_profit_factor | 0.6833 |
| gross_win_rate | 0.3886 |
| sharpe_ratio | -5.2842 |
| sortino_ratio | -1.6797 |
| max_drawdown | 0.8611 |
| cagr | -0.5411 |
| net_avg_win | 45.7619 |
| net_avg_loss | -56.8163 |
| avg_hold_time_bars | 10.7022 |
| exposure | 0.2455 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
