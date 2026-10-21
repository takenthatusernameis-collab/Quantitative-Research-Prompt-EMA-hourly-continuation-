# EMA Hourly Continuation — BABYDOGE/USDT P21_26

**Symbol:** BABYDOGE/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 10 |
| net_profit_factor | 1.3754 |
| net_win_rate | 0.6000 |
| gross_profit_factor | 1.4814 |
| gross_win_rate | 0.6000 |
| sharpe_ratio | 0.3255 |
| sortino_ratio | 0.0153 |
| max_drawdown | 0.0126 |
| cagr | 0.0063 |
| net_avg_win | 97.1462 |
| net_avg_loss | -105.9467 |
| avg_hold_time_bars | 15.4000 |
| exposure | 0.0070 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
