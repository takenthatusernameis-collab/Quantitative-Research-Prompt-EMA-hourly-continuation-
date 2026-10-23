# EMA Hourly Continuation — CTSI/USDT P89_200

**Symbol:** CTSI/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 445 |
| net_profit_factor | 0.5999 |
| net_win_rate | 0.4607 |
| gross_profit_factor | 0.9117 |
| gross_win_rate | 0.4629 |
| sharpe_ratio | -3.6514 |
| sortino_ratio | -1.0895 |
| max_drawdown | 0.7274 |
| cagr | -0.4025 |
| net_avg_win | 53.0787 |
| net_avg_loss | -75.5753 |
| avg_hold_time_bars | 11.5326 |
| exposure | 0.2333 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
