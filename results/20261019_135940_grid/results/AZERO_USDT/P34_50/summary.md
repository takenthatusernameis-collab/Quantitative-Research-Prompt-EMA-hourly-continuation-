# EMA Hourly Continuation — AZERO/USDT P34_50

**Symbol:** AZERO/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 767 |
| net_profit_factor | 0.3201 |
| net_win_rate | 0.3937 |
| gross_profit_factor | 0.7477 |
| gross_win_rate | 0.4237 |
| sharpe_ratio | -8.5678 |
| sortino_ratio | -3.3402 |
| max_drawdown | 0.9866 |
| cagr | -0.8181 |
| net_avg_win | 15.3802 |
| net_avg_loss | -31.2021 |
| avg_hold_time_bars | 4.1069 |
| exposure | 0.1425 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
