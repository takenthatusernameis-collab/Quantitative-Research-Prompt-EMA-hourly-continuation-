# EMA Hourly Continuation — MINA/USDT P144_200

**Symbol:** MINA/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 390 |
| net_profit_factor | 0.4797 |
| net_win_rate | 0.4769 |
| gross_profit_factor | 0.8857 |
| gross_win_rate | 0.4872 |
| sharpe_ratio | -4.0959 |
| sortino_ratio | -1.1388 |
| max_drawdown | 0.7692 |
| cagr | -0.4303 |
| net_avg_win | 37.5062 |
| net_avg_loss | -71.2859 |
| avg_hold_time_bars | 4.7923 |
| exposure | 0.0850 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
