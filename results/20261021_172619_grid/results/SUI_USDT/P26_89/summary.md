# EMA Hourly Continuation — SUI/USDT P26_89

**Symbol:** SUI/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 425 |
| net_profit_factor | 0.8609 |
| net_win_rate | 0.5224 |
| gross_profit_factor | 1.0789 |
| gross_win_rate | 0.5224 |
| sharpe_ratio | -0.9211 |
| sortino_ratio | -0.2733 |
| max_drawdown | 0.3581 |
| cagr | -0.1210 |
| net_avg_win | 77.1185 |
| net_avg_loss | -97.9681 |
| avg_hold_time_bars | 14.2965 |
| exposure | 0.2762 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
