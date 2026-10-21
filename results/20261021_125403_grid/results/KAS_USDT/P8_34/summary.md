# EMA Hourly Continuation — KAS/USDT P8_34

**Symbol:** KAS/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 726 |
| net_profit_factor | 0.8169 |
| net_win_rate | 0.5220 |
| gross_profit_factor | 1.0739 |
| gross_win_rate | 0.5220 |
| sharpe_ratio | -1.6360 |
| sortino_ratio | -0.6351 |
| max_drawdown | 0.5762 |
| cagr | -0.2546 |
| net_avg_win | 61.4315 |
| net_avg_loss | -82.1349 |
| avg_hold_time_bars | 8.6074 |
| exposure | 0.2840 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
