# EMA Hourly Continuation — G/USDT P12_34

**Symbol:** G/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 951 |
| net_profit_factor | 0.4827 |
| net_win_rate | 0.4501 |
| gross_profit_factor | 0.8867 |
| gross_win_rate | 0.4742 |
| sharpe_ratio | -7.3330 |
| sortino_ratio | -3.4551 |
| max_drawdown | 0.9722 |
| cagr | -0.8071 |
| net_avg_win | 21.1897 |
| net_avg_loss | -35.9240 |
| avg_hold_time_bars | 5.8791 |
| exposure | 0.2940 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
