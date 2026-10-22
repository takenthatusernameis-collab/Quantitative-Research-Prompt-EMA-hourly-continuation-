# EMA Hourly Continuation — ZEC/USDT P12_26

**Symbol:** ZEC/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1388 |
| net_profit_factor | 0.2931 |
| net_win_rate | 0.4474 |
| gross_profit_factor | 0.7105 |
| gross_win_rate | 0.4604 |
| sharpe_ratio | -9.3962 |
| sortino_ratio | -4.9386 |
| max_drawdown | 0.9979 |
| cagr | -0.9139 |
| net_avg_win | 6.6637 |
| net_avg_loss | -18.4054 |
| avg_hold_time_bars | 2.8127 |
| exposure | 0.1775 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
