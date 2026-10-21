# EMA Hourly Continuation — HBAR/USDT P20_34

**Symbol:** HBAR/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 268 |
| net_profit_factor | 0.9165 |
| net_win_rate | 0.5746 |
| gross_profit_factor | 1.3335 |
| gross_win_rate | 0.5746 |
| sharpe_ratio | -0.3893 |
| sortino_ratio | -0.0931 |
| max_drawdown | 0.1974 |
| cagr | -0.0443 |
| net_avg_win | 76.5956 |
| net_avg_loss | -112.8977 |
| avg_hold_time_bars | 5.6194 |
| exposure | 0.0685 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
