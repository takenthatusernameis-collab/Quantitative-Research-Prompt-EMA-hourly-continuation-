# EMA Hourly Continuation — AVA/USDT P34_144

**Symbol:** AVA/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 403 |
| net_profit_factor | 0.9147 |
| net_win_rate | 0.5409 |
| gross_profit_factor | 1.1590 |
| gross_win_rate | 0.5409 |
| sharpe_ratio | -0.4615 |
| sortino_ratio | -0.1341 |
| max_drawdown | 0.2915 |
| cagr | -0.0643 |
| net_avg_win | 75.5436 |
| net_avg_loss | -97.3233 |
| avg_hold_time_bars | 19.9057 |
| exposure | 0.3646 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
