# EMA Hourly Continuation — APT/USDT P12_200

**Symbol:** APT/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 251 |
| net_profit_factor | 0.7557 |
| net_win_rate | 0.5139 |
| gross_profit_factor | 1.0860 |
| gross_win_rate | 0.5219 |
| sharpe_ratio | -1.3398 |
| sortino_ratio | -0.2970 |
| max_drawdown | 0.3462 |
| cagr | -0.1349 |
| net_avg_win | 73.1431 |
| net_avg_loss | -102.3463 |
| avg_hold_time_bars | 72.0159 |
| exposure | 0.8216 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
