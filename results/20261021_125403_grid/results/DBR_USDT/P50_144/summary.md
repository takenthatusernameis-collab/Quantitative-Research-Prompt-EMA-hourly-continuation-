# EMA Hourly Continuation — DBR/USDT P50_144

**Symbol:** DBR/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 240 |
| net_profit_factor | 0.6366 |
| net_win_rate | 0.4708 |
| gross_profit_factor | 0.8804 |
| gross_win_rate | 0.4708 |
| sharpe_ratio | -2.4127 |
| sortino_ratio | -0.5945 |
| max_drawdown | 0.4467 |
| cagr | -0.2394 |
| net_avg_win | 65.5175 |
| net_avg_loss | -91.5695 |
| avg_hold_time_bars | 20.7250 |
| exposure | 0.2829 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
