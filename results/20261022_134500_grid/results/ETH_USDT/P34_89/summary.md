# EMA Hourly Continuation — ETH/USDT P34_89

**Symbol:** ETH/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 664 |
| net_profit_factor | 0.3768 |
| net_win_rate | 0.4413 |
| gross_profit_factor | 0.8641 |
| gross_win_rate | 0.4669 |
| sharpe_ratio | -7.5924 |
| sortino_ratio | -2.7585 |
| max_drawdown | 0.9731 |
| cagr | -0.7610 |
| net_avg_win | 20.0715 |
| net_avg_loss | -42.0651 |
| avg_hold_time_bars | 8.3765 |
| exposure | 0.2528 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
