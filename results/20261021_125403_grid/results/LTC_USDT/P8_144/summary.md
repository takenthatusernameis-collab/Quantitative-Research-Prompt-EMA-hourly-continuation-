# EMA Hourly Continuation — LTC/USDT P8_144

**Symbol:** LTC/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 410 |
| net_profit_factor | 0.6704 |
| net_win_rate | 0.4683 |
| gross_profit_factor | 0.8764 |
| gross_win_rate | 0.4683 |
| sharpe_ratio | -2.5108 |
| sortino_ratio | -0.7239 |
| max_drawdown | 0.5905 |
| cagr | -0.2832 |
| net_avg_win | 60.0244 |
| net_avg_loss | -78.8592 |
| avg_hold_time_bars | 36.9634 |
| exposure | 0.6889 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
