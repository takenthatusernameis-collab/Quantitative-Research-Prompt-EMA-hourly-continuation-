# EMA Hourly Continuation — ZETA/USDT P20_21

**Symbol:** ZETA/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 207 |
| net_profit_factor | 0.5572 |
| net_win_rate | 0.4541 |
| gross_profit_factor | 0.8240 |
| gross_win_rate | 0.4541 |
| sharpe_ratio | -2.5793 |
| sortino_ratio | -0.5294 |
| max_drawdown | 0.4639 |
| cagr | -0.2145 |
| net_avg_win | 61.0535 |
| net_avg_loss | -91.1539 |
| avg_hold_time_bars | 5.0773 |
| exposure | 0.0476 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
