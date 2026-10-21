# EMA Hourly Continuation — SUI/USDT P26_144

**Symbol:** SUI/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 365 |
| net_profit_factor | 0.9641 |
| net_win_rate | 0.5397 |
| gross_profit_factor | 1.1647 |
| gross_win_rate | 0.5397 |
| sharpe_ratio | -0.1661 |
| sortino_ratio | -0.0459 |
| max_drawdown | 0.2129 |
| cagr | -0.0269 |
| net_avg_win | 90.1596 |
| net_avg_loss | -109.6643 |
| avg_hold_time_bars | 26.3452 |
| exposure | 0.4371 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
