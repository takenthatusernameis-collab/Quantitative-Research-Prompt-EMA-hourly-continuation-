# EMA Hourly Continuation — ENJ/USDT P8_144

**Symbol:** ENJ/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 334 |
| net_profit_factor | 0.8450 |
| net_win_rate | 0.4970 |
| gross_profit_factor | 0.9868 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -0.9342 |
| sortino_ratio | -0.2433 |
| max_drawdown | 0.3485 |
| cagr | -0.1084 |
| net_avg_win | 82.4805 |
| net_avg_loss | -96.4532 |
| avg_hold_time_bars | 51.6018 |
| exposure | 0.7799 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
