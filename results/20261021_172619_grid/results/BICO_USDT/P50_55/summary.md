# EMA Hourly Continuation — BICO/USDT P50_55

**Symbol:** BICO/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 254 |
| net_profit_factor | 0.5215 |
| net_win_rate | 0.4488 |
| gross_profit_factor | 0.7804 |
| gross_win_rate | 0.4488 |
| sharpe_ratio | -2.9451 |
| sortino_ratio | -0.6712 |
| max_drawdown | 0.5407 |
| cagr | -0.2632 |
| net_avg_win | 51.2152 |
| net_avg_loss | -79.9615 |
| avg_hold_time_bars | 4.9409 |
| exposure | 0.0570 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
