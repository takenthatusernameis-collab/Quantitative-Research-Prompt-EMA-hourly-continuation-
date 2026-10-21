# EMA Hourly Continuation — NOT/USDT P8_34

**Symbol:** NOT/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 606 |
| net_profit_factor | 0.8054 |
| net_win_rate | 0.5033 |
| gross_profit_factor | 1.0019 |
| gross_win_rate | 0.5033 |
| sharpe_ratio | -1.6668 |
| sortino_ratio | -0.5982 |
| max_drawdown | 0.5522 |
| cagr | -0.2420 |
| net_avg_win | 66.5162 |
| net_avg_loss | -83.6808 |
| avg_hold_time_bars | 10.0215 |
| exposure | 0.2853 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
