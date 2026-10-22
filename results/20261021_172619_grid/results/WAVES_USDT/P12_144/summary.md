# EMA Hourly Continuation — WAVES/USDT P12_144

**Symbol:** WAVES/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 494 |
| net_profit_factor | 0.7647 |
| net_win_rate | 0.4980 |
| gross_profit_factor | 0.9864 |
| gross_win_rate | 0.4980 |
| sharpe_ratio | -1.8676 |
| sortino_ratio | -0.5935 |
| max_drawdown | 0.5202 |
| cagr | -0.2398 |
| net_avg_win | 65.7550 |
| net_avg_loss | -85.2924 |
| avg_hold_time_bars | 26.6053 |
| exposure | 0.5974 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
