# EMA Hourly Continuation — WIN/USDT P21_50

**Symbol:** WIN/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 928 |
| net_profit_factor | 0.3534 |
| net_win_rate | 0.3976 |
| gross_profit_factor | 0.8312 |
| gross_win_rate | 0.4246 |
| sharpe_ratio | -10.3826 |
| sortino_ratio | -4.5155 |
| max_drawdown | 0.9972 |
| cagr | -0.9025 |
| net_avg_win | 14.7705 |
| net_avg_loss | -27.5876 |
| avg_hold_time_bars | 4.6487 |
| exposure | 0.1961 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
