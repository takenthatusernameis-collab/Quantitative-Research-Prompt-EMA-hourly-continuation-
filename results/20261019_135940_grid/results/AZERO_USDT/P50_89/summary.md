# EMA Hourly Continuation — AZERO/USDT P50_89

**Symbol:** AZERO/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 575 |
| net_profit_factor | 0.5216 |
| net_win_rate | 0.4522 |
| gross_profit_factor | 0.8884 |
| gross_win_rate | 0.4591 |
| sharpe_ratio | -5.0423 |
| sortino_ratio | -1.6922 |
| max_drawdown | 0.8872 |
| cagr | -0.5652 |
| net_avg_win | 36.8081 |
| net_avg_loss | -58.2441 |
| avg_hold_time_bars | 6.4922 |
| exposure | 0.1689 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
