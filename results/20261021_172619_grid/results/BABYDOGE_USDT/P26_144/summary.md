# EMA Hourly Continuation — BABYDOGE/USDT P26_144

**Symbol:** BABYDOGE/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 61 |
| net_profit_factor | 0.9598 |
| net_win_rate | 0.5082 |
| gross_profit_factor | 1.0228 |
| gross_win_rate | 0.5082 |
| sharpe_ratio | -0.0756 |
| sortino_ratio | -0.0085 |
| max_drawdown | 0.0655 |
| cagr | -0.0049 |
| net_avg_win | 95.4781 |
| net_avg_loss | -102.7883 |
| avg_hold_time_bars | 46.9836 |
| exposure | 0.1297 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
