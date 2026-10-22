# EMA Hourly Continuation — ICP/USDT P26_100

**Symbol:** ICP/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 706 |
| net_profit_factor | 0.5915 |
| net_win_rate | 0.4816 |
| gross_profit_factor | 0.9480 |
| gross_win_rate | 0.4887 |
| sharpe_ratio | -4.2318 |
| sortino_ratio | -1.5741 |
| max_drawdown | 0.8587 |
| cagr | -0.5345 |
| net_avg_win | 36.3403 |
| net_avg_loss | -57.0775 |
| avg_hold_time_bars | 10.3598 |
| exposure | 0.3325 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
