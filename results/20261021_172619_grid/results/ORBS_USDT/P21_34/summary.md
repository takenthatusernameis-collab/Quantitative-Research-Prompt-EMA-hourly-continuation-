# EMA Hourly Continuation — ORBS/USDT P21_34

**Symbol:** ORBS/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 451 |
| net_profit_factor | 0.4635 |
| net_win_rate | 0.3969 |
| gross_profit_factor | 0.7643 |
| gross_win_rate | 0.3991 |
| sharpe_ratio | -5.8866 |
| sortino_ratio | -1.7933 |
| max_drawdown | 0.8817 |
| cagr | -0.5651 |
| net_avg_win | 42.3009 |
| net_avg_loss | -60.0597 |
| avg_hold_time_bars | 6.0931 |
| exposure | 0.1249 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
