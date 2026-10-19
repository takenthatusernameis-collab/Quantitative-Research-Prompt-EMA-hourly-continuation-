# EMA Hourly Continuation — DCR/USDT P20_89

**Symbol:** DCR/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 816 |
| net_profit_factor | 0.4855 |
| net_win_rate | 0.4424 |
| gross_profit_factor | 0.7840 |
| gross_win_rate | 0.4522 |
| sharpe_ratio | -6.0062 |
| sortino_ratio | -2.4018 |
| max_drawdown | 0.9509 |
| cagr | -0.6902 |
| net_avg_win | 24.7769 |
| net_avg_loss | -40.4933 |
| avg_hold_time_bars | 10.2708 |
| exposure | 0.3792 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
