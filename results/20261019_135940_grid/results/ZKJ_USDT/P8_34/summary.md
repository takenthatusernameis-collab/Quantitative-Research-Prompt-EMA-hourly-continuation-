# EMA Hourly Continuation — ZKJ/USDT P8_34

**Symbol:** ZKJ/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1575 |
| net_profit_factor | 0.1823 |
| net_win_rate | 0.2914 |
| gross_profit_factor | 0.4967 |
| gross_win_rate | 0.3575 |
| sharpe_ratio | -18.3738 |
| sortino_ratio | -10.5522 |
| max_drawdown | 1.0000 |
| cagr | -0.9968 |
| net_avg_win | 4.8561 |
| net_avg_loss | -10.9578 |
| avg_hold_time_bars | 5.3359 |
| exposure | 0.3820 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
