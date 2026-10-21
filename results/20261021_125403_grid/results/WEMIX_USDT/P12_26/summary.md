# EMA Hourly Continuation — WEMIX/USDT P12_26

**Symbol:** WEMIX/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 321 |
| net_profit_factor | 0.4172 |
| net_win_rate | 0.3489 |
| gross_profit_factor | 0.5609 |
| gross_win_rate | 0.3489 |
| sharpe_ratio | -5.1052 |
| sortino_ratio | -1.2937 |
| max_drawdown | 0.7841 |
| cagr | -0.4550 |
| net_avg_win | 49.9962 |
| net_avg_loss | -64.2180 |
| avg_hold_time_bars | 8.4860 |
| exposure | 0.1238 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
