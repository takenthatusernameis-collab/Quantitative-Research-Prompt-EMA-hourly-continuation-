# EMA Hourly Continuation — EUL/USDT P12_50

**Symbol:** EUL/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1026 |
| net_profit_factor | 0.4375 |
| net_win_rate | 0.4444 |
| gross_profit_factor | 0.6876 |
| gross_win_rate | 0.4503 |
| sharpe_ratio | -6.5616 |
| sortino_ratio | -2.9452 |
| max_drawdown | 0.9742 |
| cagr | -0.7623 |
| net_avg_win | 16.5969 |
| net_avg_loss | -30.3457 |
| avg_hold_time_bars | 7.7359 |
| exposure | 0.3608 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
