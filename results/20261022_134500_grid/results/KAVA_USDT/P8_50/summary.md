# EMA Hourly Continuation — KAVA/USDT P8_50

**Symbol:** KAVA/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1178 |
| net_profit_factor | 0.5683 |
| net_win_rate | 0.4397 |
| gross_profit_factor | 0.9946 |
| gross_win_rate | 0.4635 |
| sharpe_ratio | -8.3330 |
| sortino_ratio | -3.9990 |
| max_drawdown | 0.9938 |
| cagr | -0.8657 |
| net_avg_win | 25.2493 |
| net_avg_loss | -34.8706 |
| avg_hold_time_bars | 8.9720 |
| exposure | 0.4804 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
