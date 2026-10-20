# EMA Hourly Continuation — ILV/USDT P34_100

**Symbol:** ILV/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 637 |
| net_profit_factor | 0.6561 |
| net_win_rate | 0.4882 |
| gross_profit_factor | 0.9879 |
| gross_win_rate | 0.4929 |
| sharpe_ratio | -3.5791 |
| sortino_ratio | -1.2808 |
| max_drawdown | 0.7872 |
| cagr | -0.4534 |
| net_avg_win | 47.8829 |
| net_avg_loss | -69.6237 |
| avg_hold_time_bars | 10.2527 |
| exposure | 0.2969 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
