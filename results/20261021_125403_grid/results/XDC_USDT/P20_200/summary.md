# EMA Hourly Continuation — XDC/USDT P20_200

**Symbol:** XDC/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 347 |
| net_profit_factor | 0.8327 |
| net_win_rate | 0.5159 |
| gross_profit_factor | 1.0687 |
| gross_win_rate | 0.5187 |
| sharpe_ratio | -1.0538 |
| sortino_ratio | -0.2818 |
| max_drawdown | 0.2868 |
| cagr | -0.1228 |
| net_avg_win | 77.9247 |
| net_avg_loss | -99.7112 |
| avg_hold_time_bars | 35.8127 |
| exposure | 0.5649 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
