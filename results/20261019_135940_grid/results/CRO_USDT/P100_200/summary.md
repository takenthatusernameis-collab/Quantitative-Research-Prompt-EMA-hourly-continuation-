# EMA Hourly Continuation — CRO/USDT P100_200

**Symbol:** CRO/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 393 |
| net_profit_factor | 0.3866 |
| net_win_rate | 0.4300 |
| gross_profit_factor | 0.7526 |
| gross_win_rate | 0.4478 |
| sharpe_ratio | -5.1274 |
| sortino_ratio | -1.4399 |
| max_drawdown | 0.8401 |
| cagr | -0.5109 |
| net_avg_win | 31.1005 |
| net_avg_loss | -60.6982 |
| avg_hold_time_bars | 10.3639 |
| exposure | 0.1851 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
