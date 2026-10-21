# EMA Hourly Continuation — CHZ/USDT P8_26

**Symbol:** CHZ/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 684 |
| net_profit_factor | 0.7615 |
| net_win_rate | 0.5073 |
| gross_profit_factor | 1.0525 |
| gross_win_rate | 0.5073 |
| sharpe_ratio | -2.4239 |
| sortino_ratio | -0.9116 |
| max_drawdown | 0.6822 |
| cagr | -0.3408 |
| net_avg_win | 59.6961 |
| net_avg_loss | -80.7194 |
| avg_hold_time_bars | 6.5980 |
| exposure | 0.2051 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
