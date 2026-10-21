# EMA Hourly Continuation — POPCAT/USDT P26_34

**Symbol:** POPCAT/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 198 |
| net_profit_factor | 0.6952 |
| net_win_rate | 0.4798 |
| gross_profit_factor | 0.9258 |
| gross_win_rate | 0.4798 |
| sharpe_ratio | -1.8014 |
| sortino_ratio | -0.3906 |
| max_drawdown | 0.3956 |
| cagr | -0.1643 |
| net_avg_win | 77.1797 |
| net_avg_loss | -102.3947 |
| avg_hold_time_bars | 4.3384 |
| exposure | 0.0454 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
