# EMA Hourly Continuation — ZBCN/USDT P144_200

**Symbol:** ZBCN/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 151 |
| net_profit_factor | 0.8144 |
| net_win_rate | 0.5033 |
| gross_profit_factor | 1.0105 |
| gross_win_rate | 0.5033 |
| sharpe_ratio | -0.7876 |
| sortino_ratio | -0.1401 |
| max_drawdown | 0.2035 |
| cagr | -0.0630 |
| net_avg_win | 85.6025 |
| net_avg_loss | -106.5140 |
| avg_hold_time_bars | 6.1854 |
| exposure | 0.0432 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
