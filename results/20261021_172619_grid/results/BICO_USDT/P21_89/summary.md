# EMA Hourly Continuation — BICO/USDT P21_89

**Symbol:** BICO/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 542 |
| net_profit_factor | 0.7045 |
| net_win_rate | 0.4649 |
| gross_profit_factor | 0.8798 |
| gross_win_rate | 0.4649 |
| sharpe_ratio | -2.6415 |
| sortino_ratio | -0.8740 |
| max_drawdown | 0.6640 |
| cagr | -0.3314 |
| net_avg_win | 60.1671 |
| net_avg_loss | -74.2173 |
| avg_hold_time_bars | 15.7546 |
| exposure | 0.3881 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
