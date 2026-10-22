# EMA Hourly Continuation — DOGS/USDT P12_200

**Symbol:** DOGS/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 257 |
| net_profit_factor | 0.7904 |
| net_win_rate | 0.4825 |
| gross_profit_factor | 0.9308 |
| gross_win_rate | 0.4825 |
| sharpe_ratio | -1.2636 |
| sortino_ratio | -0.3117 |
| max_drawdown | 0.3334 |
| cagr | -0.1348 |
| net_avg_win | 81.3982 |
| net_avg_loss | -96.0147 |
| avg_hold_time_bars | 52.3541 |
| exposure | 0.7138 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
