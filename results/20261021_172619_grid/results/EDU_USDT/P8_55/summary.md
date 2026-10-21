# EMA Hourly Continuation — EDU/USDT P8_55

**Symbol:** EDU/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 741 |
| net_profit_factor | 0.7414 |
| net_win_rate | 0.4831 |
| gross_profit_factor | 0.9219 |
| gross_win_rate | 0.4831 |
| sharpe_ratio | -2.4508 |
| sortino_ratio | -0.9495 |
| max_drawdown | 0.6763 |
| cagr | -0.3549 |
| net_avg_win | 53.5820 |
| net_avg_loss | -67.5519 |
| avg_hold_time_bars | 14.4845 |
| exposure | 0.4857 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
