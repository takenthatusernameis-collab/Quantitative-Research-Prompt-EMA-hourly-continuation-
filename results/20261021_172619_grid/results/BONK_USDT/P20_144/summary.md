# EMA Hourly Continuation — BONK/USDT P20_144

**Symbol:** BONK/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 364 |
| net_profit_factor | 0.8456 |
| net_win_rate | 0.4973 |
| gross_profit_factor | 0.9803 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -0.9524 |
| sortino_ratio | -0.2597 |
| max_drawdown | 0.4054 |
| cagr | -0.1153 |
| net_avg_win | 80.1187 |
| net_avg_loss | -93.7091 |
| avg_hold_time_bars | 32.7335 |
| exposure | 0.5416 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
