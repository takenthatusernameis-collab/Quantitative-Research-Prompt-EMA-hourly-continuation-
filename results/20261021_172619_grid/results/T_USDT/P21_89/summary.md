# EMA Hourly Continuation — T/USDT P21_89

**Symbol:** T/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 511 |
| net_profit_factor | 0.7342 |
| net_win_rate | 0.4951 |
| gross_profit_factor | 1.0155 |
| gross_win_rate | 0.4951 |
| sharpe_ratio | -2.4795 |
| sortino_ratio | -0.8002 |
| max_drawdown | 0.6454 |
| cagr | -0.3072 |
| net_avg_win | 65.9154 |
| net_avg_loss | -88.0422 |
| avg_hold_time_bars | 15.1761 |
| exposure | 0.3509 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
