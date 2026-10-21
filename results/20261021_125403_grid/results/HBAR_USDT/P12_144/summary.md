# EMA Hourly Continuation — HBAR/USDT P12_144

**Symbol:** HBAR/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 365 |
| net_profit_factor | 0.8704 |
| net_win_rate | 0.5178 |
| gross_profit_factor | 1.0641 |
| gross_win_rate | 0.5178 |
| sharpe_ratio | -0.8087 |
| sortino_ratio | -0.2221 |
| max_drawdown | 0.3385 |
| cagr | -0.0999 |
| net_avg_win | 82.5639 |
| net_avg_loss | -101.8644 |
| avg_hold_time_bars | 39.9370 |
| exposure | 0.6626 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
