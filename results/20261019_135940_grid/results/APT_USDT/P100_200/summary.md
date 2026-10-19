# EMA Hourly Continuation — APT/USDT P100_200

**Symbol:** APT/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 380 |
| net_profit_factor | 0.4642 |
| net_win_rate | 0.4132 |
| gross_profit_factor | 0.7240 |
| gross_win_rate | 0.4158 |
| sharpe_ratio | -4.5405 |
| sortino_ratio | -1.2418 |
| max_drawdown | 0.7818 |
| cagr | -0.4527 |
| net_avg_win | 43.0453 |
| net_avg_loss | -65.2797 |
| avg_hold_time_bars | 9.0763 |
| exposure | 0.1568 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
