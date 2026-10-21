# EMA Hourly Continuation — DOGS/USDT P89_100

**Symbol:** DOGS/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 80 |
| net_profit_factor | 0.8993 |
| net_win_rate | 0.5500 |
| gross_profit_factor | 1.2067 |
| gross_win_rate | 0.5500 |
| sharpe_ratio | -0.2782 |
| sortino_ratio | -0.0390 |
| max_drawdown | 0.0892 |
| cagr | -0.0186 |
| net_avg_win | 80.4304 |
| net_avg_loss | -109.3072 |
| avg_hold_time_bars | 4.4125 |
| exposure | 0.0187 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
