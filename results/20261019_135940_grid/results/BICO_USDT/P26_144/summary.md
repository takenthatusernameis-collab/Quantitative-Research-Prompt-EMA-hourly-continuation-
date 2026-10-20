# EMA Hourly Continuation — BICO/USDT P26_144

**Symbol:** BICO/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 428 |
| net_profit_factor | 0.6263 |
| net_win_rate | 0.4533 |
| gross_profit_factor | 0.8250 |
| gross_win_rate | 0.4579 |
| sharpe_ratio | -2.8522 |
| sortino_ratio | -0.8353 |
| max_drawdown | 0.6507 |
| cagr | -0.3213 |
| net_avg_win | 53.7544 |
| net_avg_loss | -71.1514 |
| avg_hold_time_bars | 26.1238 |
| exposure | 0.5082 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
