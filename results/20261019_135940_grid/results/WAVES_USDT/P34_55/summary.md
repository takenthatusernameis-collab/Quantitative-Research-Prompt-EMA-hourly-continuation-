# EMA Hourly Continuation — WAVES/USDT P34_55

**Symbol:** WAVES/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1020 |
| net_profit_factor | 0.3332 |
| net_win_rate | 0.3814 |
| gross_profit_factor | 0.8287 |
| gross_win_rate | 0.4275 |
| sharpe_ratio | -11.4987 |
| sortino_ratio | -5.2507 |
| max_drawdown | 0.9989 |
| cagr | -0.9326 |
| net_avg_win | 12.8317 |
| net_avg_loss | -23.7403 |
| avg_hold_time_bars | 3.1696 |
| exposure | 0.1470 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
