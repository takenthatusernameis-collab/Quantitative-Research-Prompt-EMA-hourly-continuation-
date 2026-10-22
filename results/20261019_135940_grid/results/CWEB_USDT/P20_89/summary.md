# EMA Hourly Continuation — CWEB/USDT P20_89

**Symbol:** CWEB/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 551 |
| net_profit_factor | 0.4796 |
| net_win_rate | 0.4011 |
| gross_profit_factor | 0.7919 |
| gross_win_rate | 0.4102 |
| sharpe_ratio | -6.2832 |
| sortino_ratio | -2.0646 |
| max_drawdown | 0.9291 |
| cagr | -0.6477 |
| net_avg_win | 38.6603 |
| net_avg_loss | -53.9870 |
| avg_hold_time_bars | 17.7931 |
| exposure | 0.4456 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
