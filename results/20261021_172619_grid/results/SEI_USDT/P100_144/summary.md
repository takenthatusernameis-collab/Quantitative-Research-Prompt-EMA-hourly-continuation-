# EMA Hourly Continuation — SEI/USDT P100_144

**Symbol:** SEI/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 201 |
| net_profit_factor | 0.7837 |
| net_win_rate | 0.5124 |
| gross_profit_factor | 1.0368 |
| gross_win_rate | 0.5124 |
| sharpe_ratio | -1.0339 |
| sortino_ratio | -0.2110 |
| max_drawdown | 0.2605 |
| cagr | -0.0922 |
| net_avg_win | 75.8509 |
| net_avg_loss | -101.7269 |
| avg_hold_time_bars | 7.3134 |
| exposure | 0.0668 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
