# EMA Hourly Continuation — APT/USDT P26_200

**Symbol:** APT/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 323 |
| net_profit_factor | 0.7934 |
| net_win_rate | 0.5294 |
| gross_profit_factor | 1.1691 |
| gross_win_rate | 0.5418 |
| sharpe_ratio | -1.1783 |
| sortino_ratio | -0.2950 |
| max_drawdown | 0.3736 |
| cagr | -0.1357 |
| net_avg_win | 68.8290 |
| net_avg_loss | -97.6013 |
| avg_hold_time_bars | 42.2755 |
| exposure | 0.6207 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
