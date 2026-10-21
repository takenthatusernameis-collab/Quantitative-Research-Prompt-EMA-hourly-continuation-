# EMA Hourly Continuation — BDX/USDT P89_144

**Symbol:** BDX/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 219 |
| net_profit_factor | 0.4018 |
| net_win_rate | 0.4201 |
| gross_profit_factor | 0.7066 |
| gross_win_rate | 0.4247 |
| sharpe_ratio | -3.8074 |
| sortino_ratio | -0.8119 |
| max_drawdown | 0.6077 |
| cagr | -0.3111 |
| net_avg_win | 44.3657 |
| net_avg_loss | -79.9901 |
| avg_hold_time_bars | 6.5525 |
| exposure | 0.0652 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
