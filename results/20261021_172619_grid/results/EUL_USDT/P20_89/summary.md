# EMA Hourly Continuation — EUL/USDT P20_89

**Symbol:** EUL/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 463 |
| net_profit_factor | 0.7195 |
| net_win_rate | 0.4773 |
| gross_profit_factor | 0.8879 |
| gross_win_rate | 0.4773 |
| sharpe_ratio | -2.0239 |
| sortino_ratio | -0.6203 |
| max_drawdown | 0.5406 |
| cagr | -0.2485 |
| net_avg_win | 59.4167 |
| net_avg_loss | -75.4163 |
| avg_hold_time_bars | 16.8553 |
| exposure | 0.3547 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
