# EMA Hourly Continuation — BOME/USDT P89_144

**Symbol:** BOME/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 287 |
| net_profit_factor | 0.7302 |
| net_win_rate | 0.4843 |
| gross_profit_factor | 0.9126 |
| gross_win_rate | 0.4843 |
| sharpe_ratio | -1.5352 |
| sortino_ratio | -0.3716 |
| max_drawdown | 0.3857 |
| cagr | -0.1572 |
| net_avg_win | 67.9662 |
| net_avg_loss | -87.4192 |
| avg_hold_time_bars | 7.7352 |
| exposure | 0.1009 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
