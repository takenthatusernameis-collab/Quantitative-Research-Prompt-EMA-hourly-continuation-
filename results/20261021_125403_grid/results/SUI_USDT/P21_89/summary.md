# EMA Hourly Continuation — SUI/USDT P21_89

**Symbol:** SUI/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 440 |
| net_profit_factor | 0.7877 |
| net_win_rate | 0.4955 |
| gross_profit_factor | 0.9693 |
| gross_win_rate | 0.4955 |
| sharpe_ratio | -1.5363 |
| sortino_ratio | -0.4609 |
| max_drawdown | 0.4771 |
| cagr | -0.1923 |
| net_avg_win | 70.6544 |
| net_avg_loss | -88.0807 |
| avg_hold_time_bars | 16.2750 |
| exposure | 0.3255 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
