# EMA Hourly Continuation — SATS/USDT P20_21

**Symbol:** SATS/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 793 |
| net_profit_factor | 0.2071 |
| net_win_rate | 0.3632 |
| gross_profit_factor | 0.7061 |
| gross_win_rate | 0.4010 |
| sharpe_ratio | -10.9797 |
| sortino_ratio | -4.4034 |
| max_drawdown | 0.9976 |
| cagr | -0.9081 |
| net_avg_win | 9.0473 |
| net_avg_loss | -24.9136 |
| avg_hold_time_bars | 2.0744 |
| exposure | 0.0744 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
