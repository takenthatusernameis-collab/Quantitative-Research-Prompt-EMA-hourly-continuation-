# EMA Hourly Continuation — CARV/USDT P8_34

**Symbol:** CARV/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 950 |
| net_profit_factor | 0.6255 |
| net_win_rate | 0.4937 |
| gross_profit_factor | 1.0840 |
| gross_win_rate | 0.5189 |
| sharpe_ratio | -5.4816 |
| sortino_ratio | -2.6493 |
| max_drawdown | 0.9320 |
| cagr | -0.7199 |
| net_avg_win | 32.9171 |
| net_avg_loss | -51.3125 |
| avg_hold_time_bars | 7.2726 |
| exposure | 0.3888 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
