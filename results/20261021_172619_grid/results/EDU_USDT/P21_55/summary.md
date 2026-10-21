# EMA Hourly Continuation — EDU/USDT P21_55

**Symbol:** EDU/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 611 |
| net_profit_factor | 0.6485 |
| net_win_rate | 0.4746 |
| gross_profit_factor | 0.8545 |
| gross_win_rate | 0.4746 |
| sharpe_ratio | -2.9488 |
| sortino_ratio | -1.0378 |
| max_drawdown | 0.7114 |
| cagr | -0.3788 |
| net_avg_win | 44.4811 |
| net_avg_loss | -61.9652 |
| avg_hold_time_bars | 7.6039 |
| exposure | 0.2102 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
