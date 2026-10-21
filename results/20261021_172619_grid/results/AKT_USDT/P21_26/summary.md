# EMA Hourly Continuation — AKT/USDT P21_26

**Symbol:** AKT/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 150 |
| net_profit_factor | 0.7918 |
| net_win_rate | 0.5200 |
| gross_profit_factor | 1.0655 |
| gross_win_rate | 0.5200 |
| sharpe_ratio | -0.8322 |
| sortino_ratio | -0.1469 |
| max_drawdown | 0.1822 |
| cagr | -0.0653 |
| net_avg_win | 76.0887 |
| net_avg_loss | -104.1025 |
| avg_hold_time_bars | 5.3733 |
| exposure | 0.0366 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
