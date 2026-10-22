# EMA Hourly Continuation — REZ/USDT P21_34

**Symbol:** REZ/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 387 |
| net_profit_factor | 0.6820 |
| net_win_rate | 0.4677 |
| gross_profit_factor | 0.9105 |
| gross_win_rate | 0.4677 |
| sharpe_ratio | -2.6748 |
| sortino_ratio | -0.7564 |
| max_drawdown | 0.6203 |
| cagr | -0.2933 |
| net_avg_win | 68.3064 |
| net_avg_loss | -87.9959 |
| avg_hold_time_bars | 5.8579 |
| exposure | 0.1046 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
