# EMA Hourly Continuation — ANYONE/USDT P12_21

**Symbol:** ANYONE/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1276 |
| net_profit_factor | 0.3899 |
| net_win_rate | 0.3926 |
| gross_profit_factor | 0.6670 |
| gross_win_rate | 0.4052 |
| sharpe_ratio | -10.9431 |
| sortino_ratio | -5.8226 |
| max_drawdown | 0.9985 |
| cagr | -0.9426 |
| net_avg_win | 12.7342 |
| net_avg_loss | -21.1150 |
| avg_hold_time_bars | 2.7813 |
| exposure | 0.1793 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
