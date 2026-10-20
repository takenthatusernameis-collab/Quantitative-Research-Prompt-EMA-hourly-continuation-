# EMA Hourly Continuation — ARKM/USDT P12_34

**Symbol:** ARKM/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1312 |
| net_profit_factor | 0.5634 |
| net_win_rate | 0.4367 |
| gross_profit_factor | 0.9129 |
| gross_win_rate | 0.4505 |
| sharpe_ratio | -8.4990 |
| sortino_ratio | -4.3251 |
| max_drawdown | 0.9951 |
| cagr | -0.8790 |
| net_avg_win | 22.4065 |
| net_avg_loss | -30.8378 |
| avg_hold_time_bars | 4.0236 |
| exposure | 0.2400 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
