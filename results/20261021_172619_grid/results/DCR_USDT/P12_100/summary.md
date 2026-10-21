# EMA Hourly Continuation — DCR/USDT P12_100

**Symbol:** DCR/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 592 |
| net_profit_factor | 0.6966 |
| net_win_rate | 0.4747 |
| gross_profit_factor | 0.8902 |
| gross_win_rate | 0.4747 |
| sharpe_ratio | -2.6483 |
| sortino_ratio | -0.9139 |
| max_drawdown | 0.6780 |
| cagr | -0.3441 |
| net_avg_win | 53.5228 |
| net_avg_loss | -69.4178 |
| avg_hold_time_bars | 19.1182 |
| exposure | 0.5121 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
