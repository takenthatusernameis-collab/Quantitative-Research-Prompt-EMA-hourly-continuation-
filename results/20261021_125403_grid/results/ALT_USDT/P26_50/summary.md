# EMA Hourly Continuation — ALT/USDT P26_50

**Symbol:** ALT/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 522 |
| net_profit_factor | 0.6511 |
| net_win_rate | 0.4636 |
| gross_profit_factor | 0.8721 |
| gross_win_rate | 0.4636 |
| sharpe_ratio | -3.2100 |
| sortino_ratio | -1.0455 |
| max_drawdown | 0.7194 |
| cagr | -0.3810 |
| net_avg_win | 54.0017 |
| net_avg_loss | -71.6804 |
| avg_hold_time_bars | 7.0632 |
| exposure | 0.1676 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
