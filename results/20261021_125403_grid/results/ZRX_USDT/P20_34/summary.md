# EMA Hourly Continuation — ZRX/USDT P20_34

**Symbol:** ZRX/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 500 |
| net_profit_factor | 0.5748 |
| net_win_rate | 0.4740 |
| gross_profit_factor | 0.8861 |
| gross_win_rate | 0.4740 |
| sharpe_ratio | -3.9195 |
| sortino_ratio | -1.2581 |
| max_drawdown | 0.7694 |
| cagr | -0.4386 |
| net_avg_win | 43.6499 |
| net_avg_loss | -68.4367 |
| avg_hold_time_bars | 5.0760 |
| exposure | 0.1154 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
