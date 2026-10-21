# EMA Hourly Continuation — LPT/USDT P20_55

**Symbol:** LPT/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 583 |
| net_profit_factor | 0.7482 |
| net_win_rate | 0.4906 |
| gross_profit_factor | 0.9987 |
| gross_win_rate | 0.4923 |
| sharpe_ratio | -2.5743 |
| sortino_ratio | -0.8889 |
| max_drawdown | 0.6640 |
| cagr | -0.3358 |
| net_avg_win | 66.7256 |
| net_avg_loss | -85.8742 |
| avg_hold_time_bars | 8.4871 |
| exposure | 0.2249 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
