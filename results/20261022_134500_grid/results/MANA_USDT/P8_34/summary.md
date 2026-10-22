# EMA Hourly Continuation — MANA/USDT P8_34

**Symbol:** MANA/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1363 |
| net_profit_factor | 0.5073 |
| net_win_rate | 0.4409 |
| gross_profit_factor | 0.9480 |
| gross_win_rate | 0.4556 |
| sharpe_ratio | -9.5136 |
| sortino_ratio | -4.9289 |
| max_drawdown | 0.9979 |
| cagr | -0.9142 |
| net_avg_win | 17.0931 |
| net_avg_loss | -26.5773 |
| avg_hold_time_bars | 5.8247 |
| exposure | 0.3609 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
