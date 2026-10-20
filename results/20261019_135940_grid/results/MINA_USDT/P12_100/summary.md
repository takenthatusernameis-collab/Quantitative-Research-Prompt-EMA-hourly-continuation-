# EMA Hourly Continuation — MINA/USDT P12_100

**Symbol:** MINA/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 641 |
| net_profit_factor | 0.7071 |
| net_win_rate | 0.4961 |
| gross_profit_factor | 1.0354 |
| gross_win_rate | 0.5055 |
| sharpe_ratio | -2.9443 |
| sortino_ratio | -1.0492 |
| max_drawdown | 0.7518 |
| cagr | -0.3945 |
| net_avg_win | 54.3814 |
| net_avg_loss | -75.7156 |
| avg_hold_time_bars | 20.5959 |
| exposure | 0.6001 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
