# EMA Hourly Continuation — CVX/USDT P20_50

**Symbol:** CVX/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1003 |
| net_profit_factor | 0.4872 |
| net_win_rate | 0.4457 |
| gross_profit_factor | 0.8209 |
| gross_win_rate | 0.4556 |
| sharpe_ratio | -6.9040 |
| sortino_ratio | -3.0781 |
| max_drawdown | 0.9774 |
| cagr | -0.7774 |
| net_avg_win | 20.7670 |
| net_avg_loss | -34.2679 |
| avg_hold_time_bars | 4.7258 |
| exposure | 0.2155 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
