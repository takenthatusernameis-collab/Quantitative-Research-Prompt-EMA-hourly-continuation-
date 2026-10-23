# EMA Hourly Continuation — BOME/USDT P89_144

**Symbol:** BOME/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 505 |
| net_profit_factor | 0.5311 |
| net_win_rate | 0.4693 |
| gross_profit_factor | 0.8182 |
| gross_win_rate | 0.4713 |
| sharpe_ratio | -3.9377 |
| sortino_ratio | -1.2482 |
| max_drawdown | 0.7874 |
| cagr | -0.4490 |
| net_avg_win | 37.0954 |
| net_avg_loss | -61.7669 |
| avg_hold_time_bars | 5.1980 |
| exposure | 0.1193 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
