# EMA Hourly Continuation — BRETT/USDT P20_144

**Symbol:** BRETT/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 318 |
| net_profit_factor | 0.7917 |
| net_win_rate | 0.4717 |
| gross_profit_factor | 0.8936 |
| gross_win_rate | 0.4717 |
| sharpe_ratio | -1.3475 |
| sortino_ratio | -0.3514 |
| max_drawdown | 0.3403 |
| cagr | -0.1509 |
| net_avg_win | 81.4876 |
| net_avg_loss | -91.8994 |
| avg_hold_time_bars | 37.3113 |
| exposure | 0.5709 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
