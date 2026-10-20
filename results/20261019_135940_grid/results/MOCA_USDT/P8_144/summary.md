# EMA Hourly Continuation — MOCA/USDT P8_144

**Symbol:** MOCA/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 437 |
| net_profit_factor | 0.6070 |
| net_win_rate | 0.4577 |
| gross_profit_factor | 0.8907 |
| gross_win_rate | 0.4645 |
| sharpe_ratio | -3.7850 |
| sortino_ratio | -1.1595 |
| max_drawdown | 0.7497 |
| cagr | -0.4325 |
| net_avg_win | 55.9696 |
| net_avg_loss | -77.8101 |
| avg_hold_time_bars | 33.7735 |
| exposure | 0.7399 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
