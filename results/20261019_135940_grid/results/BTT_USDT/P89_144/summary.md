# EMA Hourly Continuation — BTT/USDT P89_144

**Symbol:** BTT/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 506 |
| net_profit_factor | 0.2876 |
| net_win_rate | 0.3162 |
| gross_profit_factor | 0.7829 |
| gross_win_rate | 0.4012 |
| sharpe_ratio | -10.0644 |
| sortino_ratio | -3.3515 |
| max_drawdown | 0.9891 |
| cagr | -0.8343 |
| net_avg_win | 24.9532 |
| net_avg_loss | -40.1240 |
| avg_hold_time_bars | 6.3478 |
| exposure | 0.1460 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
