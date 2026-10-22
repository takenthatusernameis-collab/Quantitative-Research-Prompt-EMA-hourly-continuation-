# EMA Hourly Continuation — BDX/USDT P26_144

**Symbol:** BDX/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1074 |
| net_profit_factor | 0.3159 |
| net_win_rate | 0.3082 |
| gross_profit_factor | 0.6962 |
| gross_win_rate | 0.3613 |
| sharpe_ratio | -14.9468 |
| sortino_ratio | -7.1652 |
| max_drawdown | 0.9999 |
| cagr | -0.9797 |
| net_avg_win | 13.9518 |
| net_avg_loss | -19.6736 |
| avg_hold_time_bars | 7.0186 |
| exposure | 0.3426 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
