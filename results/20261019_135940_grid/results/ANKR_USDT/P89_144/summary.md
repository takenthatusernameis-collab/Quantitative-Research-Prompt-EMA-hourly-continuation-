# EMA Hourly Continuation — ANKR/USDT P89_144

**Symbol:** ANKR/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 512 |
| net_profit_factor | 0.4242 |
| net_win_rate | 0.4180 |
| gross_profit_factor | 0.7987 |
| gross_win_rate | 0.4395 |
| sharpe_ratio | -6.2038 |
| sortino_ratio | -1.9855 |
| max_drawdown | 0.9160 |
| cagr | -0.6271 |
| net_avg_win | 31.5411 |
| net_avg_loss | -53.3901 |
| avg_hold_time_bars | 7.7930 |
| exposure | 0.1814 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
