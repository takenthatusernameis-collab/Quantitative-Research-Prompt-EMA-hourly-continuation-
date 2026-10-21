# EMA Hourly Continuation — TFUEL/USDT P12_144

**Symbol:** TFUEL/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 557 |
| net_profit_factor | 0.6615 |
| net_win_rate | 0.4434 |
| gross_profit_factor | 0.8275 |
| gross_win_rate | 0.4434 |
| sharpe_ratio | -3.3795 |
| sortino_ratio | -1.1270 |
| max_drawdown | 0.7321 |
| cagr | -0.4050 |
| net_avg_win | 57.7500 |
| net_avg_loss | -69.5647 |
| avg_hold_time_bars | 22.4668 |
| exposure | 0.5663 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
