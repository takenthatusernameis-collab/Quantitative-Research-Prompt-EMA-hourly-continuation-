# EMA Hourly Continuation — BTT/USDT P12_144

**Symbol:** BTT/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 308 |
| net_profit_factor | 0.6241 |
| net_win_rate | 0.4740 |
| gross_profit_factor | 0.9068 |
| gross_win_rate | 0.4740 |
| sharpe_ratio | -2.7108 |
| sortino_ratio | -0.6769 |
| max_drawdown | 0.5528 |
| cagr | -0.2713 |
| net_avg_win | 62.3618 |
| net_avg_loss | -90.0511 |
| avg_hold_time_bars | 51.6396 |
| exposure | 0.7230 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
