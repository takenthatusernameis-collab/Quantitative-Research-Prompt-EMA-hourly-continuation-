# EMA Hourly Continuation — LQTY/USDT P55_89

**Symbol:** LQTY/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 366 |
| net_profit_factor | 0.5744 |
| net_win_rate | 0.4426 |
| gross_profit_factor | 0.7850 |
| gross_win_rate | 0.4426 |
| sharpe_ratio | -3.3197 |
| sortino_ratio | -0.9018 |
| max_drawdown | 0.6511 |
| cagr | -0.3389 |
| net_avg_win | 53.9880 |
| net_avg_loss | -74.6359 |
| avg_hold_time_bars | 6.8333 |
| exposure | 0.1132 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
