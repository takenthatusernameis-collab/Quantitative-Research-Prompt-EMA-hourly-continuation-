# EMA Hourly Continuation — AIOZ/USDT P20_55

**Symbol:** AIOZ/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 511 |
| net_profit_factor | 0.7431 |
| net_win_rate | 0.4775 |
| gross_profit_factor | 0.9221 |
| gross_win_rate | 0.4775 |
| sharpe_ratio | -2.2601 |
| sortino_ratio | -0.7284 |
| max_drawdown | 0.6170 |
| cagr | -0.2848 |
| net_avg_win | 67.4816 |
| net_avg_loss | -82.9830 |
| avg_hold_time_bars | 8.8004 |
| exposure | 0.2044 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
