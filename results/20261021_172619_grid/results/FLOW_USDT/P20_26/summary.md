# EMA Hourly Continuation — FLOW/USDT P20_26

**Symbol:** FLOW/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 210 |
| net_profit_factor | 0.5693 |
| net_win_rate | 0.4619 |
| gross_profit_factor | 0.8590 |
| gross_win_rate | 0.4619 |
| sharpe_ratio | -2.5058 |
| sortino_ratio | -0.5207 |
| max_drawdown | 0.4884 |
| cagr | -0.2121 |
| net_avg_win | 61.3782 |
| net_avg_loss | -92.5508 |
| avg_hold_time_bars | 4.4619 |
| exposure | 0.0426 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
