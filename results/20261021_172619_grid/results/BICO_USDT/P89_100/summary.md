# EMA Hourly Continuation — BICO/USDT P89_100

**Symbol:** BICO/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 217 |
| net_profit_factor | 0.6193 |
| net_win_rate | 0.4839 |
| gross_profit_factor | 0.9225 |
| gross_win_rate | 0.4839 |
| sharpe_ratio | -2.1050 |
| sortino_ratio | -0.4449 |
| max_drawdown | 0.4058 |
| cagr | -0.1844 |
| net_avg_win | 62.0549 |
| net_avg_loss | -93.9443 |
| avg_hold_time_bars | 5.2120 |
| exposure | 0.0514 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
