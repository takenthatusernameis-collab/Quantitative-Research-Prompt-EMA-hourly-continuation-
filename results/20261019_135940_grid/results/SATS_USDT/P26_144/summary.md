# EMA Hourly Continuation — SATS/USDT P26_144

**Symbol:** SATS/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 506 |
| net_profit_factor | 0.5435 |
| net_win_rate | 0.4308 |
| gross_profit_factor | 0.7737 |
| gross_win_rate | 0.4348 |
| sharpe_ratio | -4.0727 |
| sortino_ratio | -1.2857 |
| max_drawdown | 0.7872 |
| cagr | -0.4541 |
| net_avg_win | 42.7461 |
| net_avg_loss | -59.5364 |
| avg_hold_time_bars | 18.0336 |
| exposure | 0.4129 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
