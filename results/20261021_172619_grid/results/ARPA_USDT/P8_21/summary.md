# EMA Hourly Continuation — ARPA/USDT P8_21

**Symbol:** ARPA/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 798 |
| net_profit_factor | 0.6453 |
| net_win_rate | 0.4862 |
| gross_profit_factor | 0.9702 |
| gross_win_rate | 0.4875 |
| sharpe_ratio | -4.2400 |
| sortino_ratio | -1.7147 |
| max_drawdown | 0.8674 |
| cagr | -0.5437 |
| net_avg_win | 40.4066 |
| net_avg_loss | -59.2578 |
| avg_hold_time_bars | 4.9912 |
| exposure | 0.1802 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
