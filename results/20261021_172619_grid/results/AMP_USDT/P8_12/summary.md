# EMA Hourly Continuation — AMP/USDT P8_12

**Symbol:** AMP/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 347 |
| net_profit_factor | 0.3543 |
| net_win_rate | 0.3545 |
| gross_profit_factor | 0.5384 |
| gross_win_rate | 0.3545 |
| sharpe_ratio | -5.7082 |
| sortino_ratio | -1.5198 |
| max_drawdown | 0.8339 |
| cagr | -0.5067 |
| net_avg_win | 37.0454 |
| net_avg_loss | -57.4159 |
| avg_hold_time_bars | 4.2997 |
| exposure | 0.0678 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
