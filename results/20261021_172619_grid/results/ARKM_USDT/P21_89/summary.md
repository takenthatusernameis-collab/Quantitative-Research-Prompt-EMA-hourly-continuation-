# EMA Hourly Continuation — ARKM/USDT P21_89

**Symbol:** ARKM/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 499 |
| net_profit_factor | 0.7698 |
| net_win_rate | 0.4810 |
| gross_profit_factor | 0.9331 |
| gross_win_rate | 0.4810 |
| sharpe_ratio | -1.9163 |
| sortino_ratio | -0.6104 |
| max_drawdown | 0.5300 |
| cagr | -0.2457 |
| net_avg_win | 70.6841 |
| net_avg_loss | -85.0884 |
| avg_hold_time_bars | 14.6814 |
| exposure | 0.3330 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
