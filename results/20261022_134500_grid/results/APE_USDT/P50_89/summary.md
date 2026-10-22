# EMA Hourly Continuation — APE/USDT P50_89

**Symbol:** APE/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 734 |
| net_profit_factor | 0.4962 |
| net_win_rate | 0.4714 |
| gross_profit_factor | 0.9110 |
| gross_win_rate | 0.4823 |
| sharpe_ratio | -5.4795 |
| sortino_ratio | -2.0924 |
| max_drawdown | 0.9231 |
| cagr | -0.6351 |
| net_avg_win | 26.2025 |
| net_avg_loss | -47.0903 |
| avg_hold_time_bars | 4.5940 |
| exposure | 0.1533 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
