# EMA Hourly Continuation — JST/USDT P20_21

**Symbol:** JST/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 203 |
| net_profit_factor | 0.3391 |
| net_win_rate | 0.4384 |
| gross_profit_factor | 0.8545 |
| gross_win_rate | 0.4778 |
| sharpe_ratio | -4.1689 |
| sortino_ratio | -0.8644 |
| max_drawdown | 0.6534 |
| cagr | -0.3430 |
| net_avg_win | 37.6712 |
| net_avg_loss | -86.7229 |
| avg_hold_time_bars | 5.0591 |
| exposure | 0.0465 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
