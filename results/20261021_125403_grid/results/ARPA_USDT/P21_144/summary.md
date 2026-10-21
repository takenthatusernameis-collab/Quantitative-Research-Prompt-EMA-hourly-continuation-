# EMA Hourly Continuation — ARPA/USDT P21_144

**Symbol:** ARPA/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 472 |
| net_profit_factor | 0.7051 |
| net_win_rate | 0.4767 |
| gross_profit_factor | 0.9070 |
| gross_win_rate | 0.4788 |
| sharpe_ratio | -2.4018 |
| sortino_ratio | -0.7419 |
| max_drawdown | 0.6083 |
| cagr | -0.2893 |
| net_avg_win | 61.3617 |
| net_avg_loss | -79.2781 |
| avg_hold_time_bars | 23.6081 |
| exposure | 0.5042 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
