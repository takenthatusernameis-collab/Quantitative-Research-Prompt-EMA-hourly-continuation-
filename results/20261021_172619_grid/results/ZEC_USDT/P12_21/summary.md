# EMA Hourly Continuation — ZEC/USDT P12_21

**Symbol:** ZEC/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 256 |
| net_profit_factor | 0.7218 |
| net_win_rate | 0.4922 |
| gross_profit_factor | 0.9602 |
| gross_win_rate | 0.4922 |
| sharpe_ratio | -1.5678 |
| sortino_ratio | -0.3594 |
| max_drawdown | 0.3509 |
| cagr | -0.1517 |
| net_avg_win | 69.7109 |
| net_avg_loss | -93.6066 |
| avg_hold_time_bars | 5.3594 |
| exposure | 0.0624 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
