# EMA Hourly Continuation — ENJ/USDT P12_55

**Symbol:** ENJ/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1013 |
| net_profit_factor | 0.5363 |
| net_win_rate | 0.4511 |
| gross_profit_factor | 0.9132 |
| gross_win_rate | 0.4669 |
| sharpe_ratio | -6.5437 |
| sortino_ratio | -2.9351 |
| max_drawdown | 0.9724 |
| cagr | -0.7585 |
| net_avg_win | 24.5956 |
| net_avg_loss | -37.6948 |
| avg_hold_time_bars | 8.0355 |
| exposure | 0.3700 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
