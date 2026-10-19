# EMA Hourly Continuation — APT/USDT P21_89

**Symbol:** APT/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 718 |
| net_profit_factor | 0.5714 |
| net_win_rate | 0.4652 |
| gross_profit_factor | 0.9302 |
| gross_win_rate | 0.4749 |
| sharpe_ratio | -4.8327 |
| sortino_ratio | -1.8169 |
| max_drawdown | 0.8987 |
| cagr | -0.5864 |
| net_avg_win | 35.5724 |
| net_avg_loss | -54.1460 |
| avg_hold_time_bars | 11.3635 |
| exposure | 0.3709 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
