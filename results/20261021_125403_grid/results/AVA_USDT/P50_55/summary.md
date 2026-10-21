# EMA Hourly Continuation — AVA/USDT P50_55

**Symbol:** AVA/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 107 |
| net_profit_factor | 0.6821 |
| net_win_rate | 0.5140 |
| gross_profit_factor | 1.0401 |
| gross_win_rate | 0.5140 |
| sharpe_ratio | -1.1648 |
| sortino_ratio | -0.1739 |
| max_drawdown | 0.1797 |
| cagr | -0.0758 |
| net_avg_win | 70.0872 |
| net_avg_loss | -108.6802 |
| avg_hold_time_bars | 3.6168 |
| exposure | 0.0176 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
