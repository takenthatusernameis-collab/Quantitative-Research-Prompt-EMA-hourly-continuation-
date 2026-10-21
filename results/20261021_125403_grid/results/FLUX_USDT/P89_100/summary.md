# EMA Hourly Continuation — FLUX/USDT P89_100

**Symbol:** FLUX/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 103 |
| net_profit_factor | 0.7210 |
| net_win_rate | 0.5049 |
| gross_profit_factor | 1.0162 |
| gross_win_rate | 0.5049 |
| sharpe_ratio | -1.0313 |
| sortino_ratio | -0.1505 |
| max_drawdown | 0.1816 |
| cagr | -0.0670 |
| net_avg_win | 79.4484 |
| net_avg_loss | -112.3598 |
| avg_hold_time_bars | 4.2621 |
| exposure | 0.0200 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
