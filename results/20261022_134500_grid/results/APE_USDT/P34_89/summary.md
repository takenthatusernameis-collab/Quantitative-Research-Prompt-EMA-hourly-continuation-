# EMA Hourly Continuation — APE/USDT P34_89

**Symbol:** APE/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 723 |
| net_profit_factor | 0.5644 |
| net_win_rate | 0.4772 |
| gross_profit_factor | 0.9541 |
| gross_win_rate | 0.4869 |
| sharpe_ratio | -4.7205 |
| sortino_ratio | -1.7763 |
| max_drawdown | 0.8907 |
| cagr | -0.5786 |
| net_avg_win | 33.2713 |
| net_avg_loss | -53.8023 |
| avg_hold_time_bars | 7.0360 |
| exposure | 0.2312 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
