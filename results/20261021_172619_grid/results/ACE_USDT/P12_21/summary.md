# EMA Hourly Continuation — ACE/USDT P12_21

**Symbol:** ACE/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 491 |
| net_profit_factor | 0.7216 |
| net_win_rate | 0.5071 |
| gross_profit_factor | 1.0925 |
| gross_win_rate | 0.5132 |
| sharpe_ratio | -2.4999 |
| sortino_ratio | -0.7946 |
| max_drawdown | 0.6009 |
| cagr | -0.3043 |
| net_avg_win | 62.4215 |
| net_avg_loss | -89.0033 |
| avg_hold_time_bars | 6.2770 |
| exposure | 0.1395 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
