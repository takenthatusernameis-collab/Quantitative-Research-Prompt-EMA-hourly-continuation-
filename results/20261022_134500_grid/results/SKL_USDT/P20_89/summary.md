# EMA Hourly Continuation — SKL/USDT P20_89

**Symbol:** SKL/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 713 |
| net_profit_factor | 0.6673 |
| net_win_rate | 0.4895 |
| gross_profit_factor | 1.0094 |
| gross_win_rate | 0.4965 |
| sharpe_ratio | -3.6323 |
| sortino_ratio | -1.3681 |
| max_drawdown | 0.8146 |
| cagr | -0.4783 |
| net_avg_win | 46.2629 |
| net_avg_loss | -66.4674 |
| avg_hold_time_bars | 12.5035 |
| exposure | 0.4052 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
