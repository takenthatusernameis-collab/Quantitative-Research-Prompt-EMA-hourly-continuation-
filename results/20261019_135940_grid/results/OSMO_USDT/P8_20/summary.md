# EMA Hourly Continuation — OSMO/USDT P8_20

**Symbol:** OSMO/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1643 |
| net_profit_factor | 0.4604 |
| net_win_rate | 0.4181 |
| gross_profit_factor | 1.1643 |
| gross_win_rate | 0.4449 |
| sharpe_ratio | -12.6857 |
| sortino_ratio | -7.2604 |
| max_drawdown | 0.9999 |
| cagr | -0.9756 |
| net_avg_win | 12.4197 |
| net_avg_loss | -19.3844 |
| avg_hold_time_bars | 3.3183 |
| exposure | 0.2478 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
