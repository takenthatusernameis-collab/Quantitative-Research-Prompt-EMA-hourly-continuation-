# EMA Hourly Continuation — ZEC/USDT P20_89

**Symbol:** ZEC/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 701 |
| net_profit_factor | 0.6134 |
| net_win_rate | 0.4850 |
| gross_profit_factor | 0.9510 |
| gross_win_rate | 0.4922 |
| sharpe_ratio | -3.6959 |
| sortino_ratio | -1.3818 |
| max_drawdown | 0.8138 |
| cagr | -0.4829 |
| net_avg_win | 37.7636 |
| net_avg_loss | -57.9797 |
| avg_hold_time_bars | 11.7033 |
| exposure | 0.3729 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
