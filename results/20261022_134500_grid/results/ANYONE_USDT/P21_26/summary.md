# EMA Hourly Continuation — ANYONE/USDT P21_26

**Symbol:** ANYONE/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1005 |
| net_profit_factor | 0.3226 |
| net_win_rate | 0.3731 |
| gross_profit_factor | 0.6593 |
| gross_win_rate | 0.3910 |
| sharpe_ratio | -11.6619 |
| sortino_ratio | -5.5512 |
| max_drawdown | 0.9983 |
| cagr | -0.9409 |
| net_avg_win | 12.6773 |
| net_avg_loss | -23.3924 |
| avg_hold_time_bars | 2.3692 |
| exposure | 0.1203 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
