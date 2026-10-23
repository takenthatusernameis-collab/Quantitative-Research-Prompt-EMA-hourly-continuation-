# EMA Hourly Continuation — PUFFER/USDT P100_200

**Symbol:** PUFFER/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 278 |
| net_profit_factor | 0.5740 |
| net_win_rate | 0.4496 |
| gross_profit_factor | 0.8331 |
| gross_win_rate | 0.4532 |
| sharpe_ratio | -3.2587 |
| sortino_ratio | -0.8485 |
| max_drawdown | 0.5619 |
| cagr | -0.3324 |
| net_avg_win | 60.0851 |
| net_avg_loss | -85.5163 |
| avg_hold_time_bars | 10.5899 |
| exposure | 0.1666 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
