# EMA Hourly Continuation — NOT/USDT P21_200

**Symbol:** NOT/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 286 |
| net_profit_factor | 0.7476 |
| net_win_rate | 0.4720 |
| gross_profit_factor | 0.8770 |
| gross_win_rate | 0.4720 |
| sharpe_ratio | -1.4576 |
| sortino_ratio | -0.3563 |
| max_drawdown | 0.3672 |
| cagr | -0.1517 |
| net_avg_win | 72.3119 |
| net_avg_loss | -86.4730 |
| avg_hold_time_bars | 46.1503 |
| exposure | 0.6200 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
