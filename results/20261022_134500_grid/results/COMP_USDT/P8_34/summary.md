# EMA Hourly Continuation — COMP/USDT P8_34

**Symbol:** COMP/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1392 |
| net_profit_factor | 0.4041 |
| net_win_rate | 0.4425 |
| gross_profit_factor | 0.8189 |
| gross_win_rate | 0.4655 |
| sharpe_ratio | -9.2954 |
| sortino_ratio | -4.8718 |
| max_drawdown | 0.9976 |
| cagr | -0.9101 |
| net_avg_win | 10.9835 |
| net_avg_loss | -21.5751 |
| avg_hold_time_bars | 5.7126 |
| exposure | 0.3615 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
