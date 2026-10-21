# EMA Hourly Continuation — WIN/USDT P26_100

**Symbol:** WIN/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 371 |
| net_profit_factor | 0.7774 |
| net_win_rate | 0.5229 |
| gross_profit_factor | 1.0748 |
| gross_win_rate | 0.5229 |
| sharpe_ratio | -1.3995 |
| sortino_ratio | -0.3881 |
| max_drawdown | 0.4639 |
| cagr | -0.1645 |
| net_avg_win | 65.3892 |
| net_avg_loss | -92.1866 |
| avg_hold_time_bars | 19.5337 |
| exposure | 0.3294 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
