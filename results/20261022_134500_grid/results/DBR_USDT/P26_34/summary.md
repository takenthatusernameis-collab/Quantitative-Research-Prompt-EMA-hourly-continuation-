# EMA Hourly Continuation — DBR/USDT P26_34

**Symbol:** DBR/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 677 |
| net_profit_factor | 0.3337 |
| net_win_rate | 0.3826 |
| gross_profit_factor | 1.0347 |
| gross_win_rate | 0.4549 |
| sharpe_ratio | -10.8311 |
| sortino_ratio | -4.5420 |
| max_drawdown | 0.9913 |
| cagr | -0.9059 |
| net_avg_win | 19.1680 |
| net_avg_loss | -35.5921 |
| avg_hold_time_bars | 3.8065 |
| exposure | 0.1465 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
