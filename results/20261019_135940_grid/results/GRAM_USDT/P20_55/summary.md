# EMA Hourly Continuation — GRAM/USDT P20_55

**Symbol:** GRAM/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1000 |
| net_profit_factor | 0.3716 |
| net_win_rate | 0.4220 |
| gross_profit_factor | 0.8224 |
| gross_win_rate | 0.4490 |
| sharpe_ratio | -9.3126 |
| sortino_ratio | -4.1609 |
| max_drawdown | 0.9949 |
| cagr | -0.8762 |
| net_avg_win | 13.9410 |
| net_avg_loss | -27.3882 |
| avg_hold_time_bars | 5.0630 |
| exposure | 0.2301 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
