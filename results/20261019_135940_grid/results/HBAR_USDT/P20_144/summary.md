# EMA Hourly Continuation — HBAR/USDT P20_144

**Symbol:** HBAR/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 473 |
| net_profit_factor | 0.6668 |
| net_win_rate | 0.4989 |
| gross_profit_factor | 1.0438 |
| gross_win_rate | 0.5116 |
| sharpe_ratio | -2.6680 |
| sortino_ratio | -0.8147 |
| max_drawdown | 0.6558 |
| cagr | -0.3244 |
| net_avg_win | 53.1272 |
| net_avg_loss | -79.3386 |
| avg_hold_time_bars | 26.9281 |
| exposure | 0.5790 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
