# EMA Hourly Continuation — PUNDIX/USDT P55_144

**Symbol:** PUNDIX/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 488 |
| net_profit_factor | 0.5618 |
| net_win_rate | 0.4693 |
| gross_profit_factor | 0.9174 |
| gross_win_rate | 0.4775 |
| sharpe_ratio | -4.0355 |
| sortino_ratio | -1.2592 |
| max_drawdown | 0.7822 |
| cagr | -0.4513 |
| net_avg_win | 43.5810 |
| net_avg_loss | -68.5902 |
| avg_hold_time_bars | 12.0184 |
| exposure | 0.2666 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
