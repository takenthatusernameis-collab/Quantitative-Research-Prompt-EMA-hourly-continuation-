# EMA Hourly Continuation — XAI/USDT P50_144

**Symbol:** XAI/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 372 |
| net_profit_factor | 0.7253 |
| net_win_rate | 0.4704 |
| gross_profit_factor | 0.8897 |
| gross_win_rate | 0.4704 |
| sharpe_ratio | -2.0185 |
| sortino_ratio | -0.5541 |
| max_drawdown | 0.5551 |
| cagr | -0.2255 |
| net_avg_win | 71.4621 |
| net_avg_loss | -87.5239 |
| avg_hold_time_bars | 20.1452 |
| exposure | 0.3406 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
