# EMA Hourly Continuation — XPR/USDT P21_200

**Symbol:** XPR/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 288 |
| net_profit_factor | 0.8527 |
| net_win_rate | 0.5104 |
| gross_profit_factor | 1.0189 |
| gross_win_rate | 0.5104 |
| sharpe_ratio | -0.7503 |
| sortino_ratio | -0.1824 |
| max_drawdown | 0.2238 |
| cagr | -0.0826 |
| net_avg_win | 76.6330 |
| net_avg_loss | -93.6981 |
| avg_hold_time_bars | 42.6528 |
| exposure | 0.5584 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
