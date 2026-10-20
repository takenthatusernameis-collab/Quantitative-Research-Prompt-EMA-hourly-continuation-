# EMA Hourly Continuation — GTC/USDT P21_50

**Symbol:** GTC/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 932 |
| net_profit_factor | 0.4872 |
| net_win_rate | 0.4410 |
| gross_profit_factor | 0.8760 |
| gross_win_rate | 0.4549 |
| sharpe_ratio | -7.0882 |
| sortino_ratio | -3.0443 |
| max_drawdown | 0.9762 |
| cagr | -0.7716 |
| net_avg_win | 22.5475 |
| net_avg_loss | -36.5101 |
| avg_hold_time_bars | 5.2704 |
| exposure | 0.2233 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
