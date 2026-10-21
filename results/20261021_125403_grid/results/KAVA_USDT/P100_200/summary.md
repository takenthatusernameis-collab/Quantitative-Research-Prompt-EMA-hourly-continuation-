# EMA Hourly Continuation — KAVA/USDT P100_200

**Symbol:** KAVA/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 282 |
| net_profit_factor | 0.6250 |
| net_win_rate | 0.4645 |
| gross_profit_factor | 0.8915 |
| gross_win_rate | 0.4681 |
| sharpe_ratio | -2.6929 |
| sortino_ratio | -0.6375 |
| max_drawdown | 0.5544 |
| cagr | -0.2626 |
| net_avg_win | 68.0055 |
| net_avg_loss | -94.4045 |
| avg_hold_time_bars | 13.2908 |
| exposure | 0.1704 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
