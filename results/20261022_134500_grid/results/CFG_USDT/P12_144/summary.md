# EMA Hourly Continuation — CFG/USDT P12_144

**Symbol:** CFG/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 422 |
| net_profit_factor | 0.6370 |
| net_win_rate | 0.4597 |
| gross_profit_factor | 0.8557 |
| gross_win_rate | 0.4645 |
| sharpe_ratio | -2.7024 |
| sortino_ratio | -0.7835 |
| max_drawdown | 0.6138 |
| cagr | -0.3075 |
| net_avg_win | 54.5094 |
| net_avg_loss | -72.8121 |
| avg_hold_time_bars | 38.3673 |
| exposure | 0.7360 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
