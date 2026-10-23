# EMA Hourly Continuation — KNC/USDT P100_200

**Symbol:** KNC/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 357 |
| net_profit_factor | 0.5964 |
| net_win_rate | 0.4874 |
| gross_profit_factor | 1.0009 |
| gross_win_rate | 0.4930 |
| sharpe_ratio | -3.3153 |
| sortino_ratio | -0.8673 |
| max_drawdown | 0.6783 |
| cagr | -0.3569 |
| net_avg_win | 56.8953 |
| net_avg_loss | -90.7064 |
| avg_hold_time_bars | 10.6162 |
| exposure | 0.1723 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
