# EMA Hourly Continuation — XNO/USDT P20_144

**Symbol:** XNO/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 461 |
| net_profit_factor | 0.6817 |
| net_win_rate | 0.4534 |
| gross_profit_factor | 0.8366 |
| gross_win_rate | 0.4534 |
| sharpe_ratio | -2.6889 |
| sortino_ratio | -0.8190 |
| max_drawdown | 0.6126 |
| cagr | -0.3143 |
| net_avg_win | 62.7526 |
| net_avg_loss | -76.3445 |
| avg_hold_time_bars | 22.4035 |
| exposure | 0.4695 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
