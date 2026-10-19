# EMA Hourly Continuation — RENDER/USDT P20_50

**Symbol:** RENDER/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 896 |
| net_profit_factor | 0.5250 |
| net_win_rate | 0.4542 |
| gross_profit_factor | 0.8871 |
| gross_win_rate | 0.4732 |
| sharpe_ratio | -6.9841 |
| sortino_ratio | -3.1871 |
| max_drawdown | 0.9655 |
| cagr | -0.7844 |
| net_avg_win | 26.1692 |
| net_avg_loss | -41.4905 |
| avg_hold_time_bars | 4.0725 |
| exposure | 0.1926 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
