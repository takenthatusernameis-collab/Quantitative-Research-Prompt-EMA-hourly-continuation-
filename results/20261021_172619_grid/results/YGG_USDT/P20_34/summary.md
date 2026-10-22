# EMA Hourly Continuation — YGG/USDT P20_34

**Symbol:** YGG/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 417 |
| net_profit_factor | 0.6156 |
| net_win_rate | 0.4508 |
| gross_profit_factor | 0.8437 |
| gross_win_rate | 0.4508 |
| sharpe_ratio | -3.4102 |
| sortino_ratio | -0.9904 |
| max_drawdown | 0.6925 |
| cagr | -0.3659 |
| net_avg_win | 58.1921 |
| net_avg_loss | -77.6008 |
| avg_hold_time_bars | 4.7794 |
| exposure | 0.0902 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
