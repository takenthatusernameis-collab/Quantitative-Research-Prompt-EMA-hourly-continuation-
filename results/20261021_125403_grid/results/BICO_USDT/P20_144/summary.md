# EMA Hourly Continuation — BICO/USDT P20_144

**Symbol:** BICO/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 379 |
| net_profit_factor | 0.7782 |
| net_win_rate | 0.4802 |
| gross_profit_factor | 0.9196 |
| gross_win_rate | 0.4802 |
| sharpe_ratio | -1.5102 |
| sortino_ratio | -0.4186 |
| max_drawdown | 0.4558 |
| cagr | -0.1763 |
| net_avg_win | 74.3426 |
| net_avg_loss | -88.2541 |
| avg_hold_time_bars | 32.4248 |
| exposure | 0.5586 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
