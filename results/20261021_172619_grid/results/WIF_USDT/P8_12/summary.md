# EMA Hourly Continuation — WIF/USDT P8_12

**Symbol:** WIF/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 200 |
| net_profit_factor | 0.9091 |
| net_win_rate | 0.5350 |
| gross_profit_factor | 1.1515 |
| gross_win_rate | 0.5350 |
| sharpe_ratio | -0.4321 |
| sortino_ratio | -0.0883 |
| max_drawdown | 0.2693 |
| cagr | -0.0418 |
| net_avg_win | 95.0982 |
| net_avg_loss | -120.3498 |
| avg_hold_time_bars | 4.8550 |
| exposure | 0.0441 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
