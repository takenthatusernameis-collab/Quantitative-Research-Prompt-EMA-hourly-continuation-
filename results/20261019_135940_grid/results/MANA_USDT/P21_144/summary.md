# EMA Hourly Continuation — MANA/USDT P21_144

**Symbol:** MANA/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 473 |
| net_profit_factor | 0.6259 |
| net_win_rate | 0.4672 |
| gross_profit_factor | 0.9186 |
| gross_win_rate | 0.4693 |
| sharpe_ratio | -3.5213 |
| sortino_ratio | -1.0705 |
| max_drawdown | 0.7403 |
| cagr | -0.4071 |
| net_avg_win | 55.3255 |
| net_avg_loss | -77.5241 |
| avg_hold_time_bars | 26.0867 |
| exposure | 0.5609 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
