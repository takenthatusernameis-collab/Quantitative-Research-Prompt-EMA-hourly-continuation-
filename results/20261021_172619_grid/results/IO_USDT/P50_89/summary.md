# EMA Hourly Continuation — IO/USDT P50_89

**Symbol:** IO/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 310 |
| net_profit_factor | 0.6760 |
| net_win_rate | 0.4581 |
| gross_profit_factor | 0.8457 |
| gross_win_rate | 0.4581 |
| sharpe_ratio | -2.2548 |
| sortino_ratio | -0.5826 |
| max_drawdown | 0.4871 |
| cagr | -0.2346 |
| net_avg_win | 68.7219 |
| net_avg_loss | -85.9206 |
| avg_hold_time_bars | 6.9097 |
| exposure | 0.1037 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
