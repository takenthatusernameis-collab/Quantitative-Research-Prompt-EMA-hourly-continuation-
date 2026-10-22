# EMA Hourly Continuation — ZEC/USDT P20_26

**Symbol:** ZEC/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1143 |
| net_profit_factor | 0.1440 |
| net_win_rate | 0.3718 |
| gross_profit_factor | 0.5605 |
| gross_win_rate | 0.4007 |
| sharpe_ratio | -13.1741 |
| sortino_ratio | -6.4153 |
| max_drawdown | 0.9998 |
| cagr | -0.9669 |
| net_avg_win | 3.9590 |
| net_avg_loss | -16.2683 |
| avg_hold_time_bars | 1.8985 |
| exposure | 0.0986 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
