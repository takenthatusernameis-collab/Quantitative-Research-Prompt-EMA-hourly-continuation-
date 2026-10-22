# EMA Hourly Continuation — TIA/USDT P26_144

**Symbol:** TIA/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 447 |
| net_profit_factor | 0.6519 |
| net_win_rate | 0.4609 |
| gross_profit_factor | 0.9135 |
| gross_win_rate | 0.4743 |
| sharpe_ratio | -2.9250 |
| sortino_ratio | -0.8697 |
| max_drawdown | 0.6549 |
| cagr | -0.3384 |
| net_avg_win | 58.7006 |
| net_avg_loss | -76.9648 |
| avg_hold_time_bars | 24.3221 |
| exposure | 0.4942 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
