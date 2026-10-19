# EMA Hourly Continuation — ICP/USDT P50_200

**Symbol:** ICP/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 382 |
| net_profit_factor | 0.6280 |
| net_win_rate | 0.4817 |
| gross_profit_factor | 0.9456 |
| gross_win_rate | 0.4869 |
| sharpe_ratio | -2.9845 |
| sortino_ratio | -0.8144 |
| max_drawdown | 0.6448 |
| cagr | -0.3280 |
| net_avg_win | 57.9482 |
| net_avg_loss | -85.7459 |
| avg_hold_time_bars | 24.1178 |
| exposure | 0.4188 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
