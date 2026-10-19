# EMA Hourly Continuation — GRAM/USDT P12_89

**Symbol:** GRAM/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 761 |
| net_profit_factor | 0.4700 |
| net_win_rate | 0.4573 |
| gross_profit_factor | 0.8912 |
| gross_win_rate | 0.4744 |
| sharpe_ratio | -6.0650 |
| sortino_ratio | -2.3337 |
| max_drawdown | 0.9495 |
| cagr | -0.6866 |
| net_avg_win | 24.1029 |
| net_avg_loss | -43.2087 |
| avg_hold_time_bars | 15.3101 |
| exposure | 0.5296 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
