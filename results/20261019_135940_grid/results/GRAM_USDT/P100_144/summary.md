# EMA Hourly Continuation — GRAM/USDT P100_144

**Symbol:** GRAM/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 506 |
| net_profit_factor | 0.3424 |
| net_win_rate | 0.4427 |
| gross_profit_factor | 0.8475 |
| gross_win_rate | 0.4644 |
| sharpe_ratio | -6.6681 |
| sortino_ratio | -2.1354 |
| max_drawdown | 0.9368 |
| cagr | -0.6659 |
| net_avg_win | 21.7619 |
| net_avg_loss | -50.4875 |
| avg_hold_time_bars | 4.1522 |
| exposure | 0.0955 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
