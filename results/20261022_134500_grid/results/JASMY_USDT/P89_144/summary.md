# EMA Hourly Continuation — JASMY/USDT P89_144

**Symbol:** JASMY/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 485 |
| net_profit_factor | 0.6531 |
| net_win_rate | 0.5258 |
| gross_profit_factor | 1.1244 |
| gross_win_rate | 0.5320 |
| sharpe_ratio | -2.8944 |
| sortino_ratio | -0.8984 |
| max_drawdown | 0.6779 |
| cagr | -0.3543 |
| net_avg_win | 49.2122 |
| net_avg_loss | -83.5476 |
| avg_hold_time_bars | 5.1835 |
| exposure | 0.1143 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
