# EMA Hourly Continuation — MANA/USDT P55_100

**Symbol:** MANA/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 343 |
| net_profit_factor | 0.6727 |
| net_win_rate | 0.4810 |
| gross_profit_factor | 0.9232 |
| gross_win_rate | 0.4810 |
| sharpe_ratio | -2.2801 |
| sortino_ratio | -0.6043 |
| max_drawdown | 0.5044 |
| cagr | -0.2415 |
| net_avg_win | 62.3431 |
| net_avg_loss | -85.9099 |
| avg_hold_time_bars | 8.1866 |
| exposure | 0.1276 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
