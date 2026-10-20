# EMA Hourly Continuation — LPT/USDT P12_144

**Symbol:** LPT/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 508 |
| net_profit_factor | 0.6953 |
| net_win_rate | 0.4744 |
| gross_profit_factor | 0.9597 |
| gross_win_rate | 0.4783 |
| sharpe_ratio | -2.9673 |
| sortino_ratio | -0.9419 |
| max_drawdown | 0.6998 |
| cagr | -0.3593 |
| net_avg_win | 63.7387 |
| net_avg_loss | -82.7403 |
| avg_hold_time_bars | 29.0906 |
| exposure | 0.6717 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
