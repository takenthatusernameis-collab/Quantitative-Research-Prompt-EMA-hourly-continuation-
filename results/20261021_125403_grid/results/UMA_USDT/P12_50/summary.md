# EMA Hourly Continuation — UMA/USDT P12_50

**Symbol:** UMA/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 696 |
| net_profit_factor | 0.6545 |
| net_win_rate | 0.4698 |
| gross_profit_factor | 0.8795 |
| gross_win_rate | 0.4698 |
| sharpe_ratio | -3.6634 |
| sortino_ratio | -1.3776 |
| max_drawdown | 0.8021 |
| cagr | -0.4682 |
| net_avg_win | 46.0750 |
| net_avg_loss | -62.3817 |
| avg_hold_time_bars | 9.7543 |
| exposure | 0.3086 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
