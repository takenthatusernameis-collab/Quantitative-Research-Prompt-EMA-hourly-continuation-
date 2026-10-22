# EMA Hourly Continuation — SATS/USDT P89_100

**Symbol:** SATS/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 123 |
| net_profit_factor | 0.4543 |
| net_win_rate | 0.3902 |
| gross_profit_factor | 0.6424 |
| gross_win_rate | 0.3902 |
| sharpe_ratio | -2.6750 |
| sortino_ratio | -0.4203 |
| max_drawdown | 0.4046 |
| cagr | -0.1779 |
| net_avg_win | 67.6135 |
| net_avg_loss | -95.2606 |
| avg_hold_time_bars | 5.7154 |
| exposure | 0.0318 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
