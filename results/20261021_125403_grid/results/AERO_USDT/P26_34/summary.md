# EMA Hourly Continuation — AERO/USDT P26_34

**Symbol:** AERO/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 159 |
| net_profit_factor | 0.7353 |
| net_win_rate | 0.5031 |
| gross_profit_factor | 1.0116 |
| gross_win_rate | 0.5031 |
| sharpe_ratio | -1.2123 |
| sortino_ratio | -0.2196 |
| max_drawdown | 0.2369 |
| cagr | -0.0954 |
| net_avg_win | 77.3044 |
| net_avg_loss | -106.4673 |
| avg_hold_time_bars | 4.5912 |
| exposure | 0.0332 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
