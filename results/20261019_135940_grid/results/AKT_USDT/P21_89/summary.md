# EMA Hourly Continuation — AKT/USDT P21_89

**Symbol:** AKT/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 743 |
| net_profit_factor | 0.5932 |
| net_win_rate | 0.4657 |
| gross_profit_factor | 0.9129 |
| gross_win_rate | 0.4764 |
| sharpe_ratio | -4.5004 |
| sortino_ratio | -1.7193 |
| max_drawdown | 0.8775 |
| cagr | -0.5635 |
| net_avg_win | 36.8861 |
| net_avg_loss | -54.1950 |
| avg_hold_time_bars | 10.2638 |
| exposure | 0.3466 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
