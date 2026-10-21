# EMA Hourly Continuation — BICO/USDT P89_200

**Symbol:** BICO/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 297 |
| net_profit_factor | 0.7367 |
| net_win_rate | 0.4680 |
| gross_profit_factor | 0.8956 |
| gross_win_rate | 0.4680 |
| sharpe_ratio | -1.7527 |
| sortino_ratio | -0.4296 |
| max_drawdown | 0.4215 |
| cagr | -0.1797 |
| net_avg_win | 78.8937 |
| net_avg_loss | -94.2100 |
| avg_hold_time_bars | 16.4613 |
| exposure | 0.2222 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
