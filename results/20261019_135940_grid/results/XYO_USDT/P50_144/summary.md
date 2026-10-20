# EMA Hourly Continuation — XYO/USDT P50_144

**Symbol:** XYO/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 631 |
| net_profit_factor | 0.4216 |
| net_win_rate | 0.3978 |
| gross_profit_factor | 0.7116 |
| gross_win_rate | 0.4073 |
| sharpe_ratio | -7.0142 |
| sortino_ratio | -2.4639 |
| max_drawdown | 0.9580 |
| cagr | -0.7122 |
| net_avg_win | 27.7852 |
| net_avg_loss | -43.5319 |
| avg_hold_time_bars | 9.9683 |
| exposure | 0.2846 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
