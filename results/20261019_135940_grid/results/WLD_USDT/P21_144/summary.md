# EMA Hourly Continuation — WLD/USDT P21_144

**Symbol:** WLD/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 421 |
| net_profit_factor | 0.8636 |
| net_win_rate | 0.5249 |
| gross_profit_factor | 1.0975 |
| gross_win_rate | 0.5249 |
| sharpe_ratio | -0.8746 |
| sortino_ratio | -0.2560 |
| max_drawdown | 0.3522 |
| cagr | -0.1166 |
| net_avg_win | 76.6537 |
| net_avg_loss | -98.0762 |
| avg_hold_time_bars | 29.0000 |
| exposure | 0.5550 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
