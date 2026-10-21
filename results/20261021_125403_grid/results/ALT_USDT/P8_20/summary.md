# EMA Hourly Continuation — ALT/USDT P8_20

**Symbol:** ALT/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 734 |
| net_profit_factor | 0.6714 |
| net_win_rate | 0.4755 |
| gross_profit_factor | 0.9158 |
| gross_win_rate | 0.4755 |
| sharpe_ratio | -3.6131 |
| sortino_ratio | -1.3989 |
| max_drawdown | 0.8258 |
| cagr | -0.4737 |
| net_avg_win | 46.8675 |
| net_avg_loss | -63.2775 |
| avg_hold_time_bars | 5.9142 |
| exposure | 0.1973 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
