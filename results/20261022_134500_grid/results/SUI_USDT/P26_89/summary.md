# EMA Hourly Continuation — SUI/USDT P26_89

**Symbol:** SUI/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 724 |
| net_profit_factor | 0.6049 |
| net_win_rate | 0.4738 |
| gross_profit_factor | 0.9496 |
| gross_win_rate | 0.4848 |
| sharpe_ratio | -4.7584 |
| sortino_ratio | -1.7974 |
| max_drawdown | 0.8974 |
| cagr | -0.5855 |
| net_avg_win | 39.7515 |
| net_avg_loss | -59.1583 |
| avg_hold_time_bars | 9.1754 |
| exposure | 0.3020 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
