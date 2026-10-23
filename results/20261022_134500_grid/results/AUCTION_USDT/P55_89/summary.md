# EMA Hourly Continuation — AUCTION/USDT P55_89

**Symbol:** AUCTION/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 666 |
| net_profit_factor | 0.4283 |
| net_win_rate | 0.4264 |
| gross_profit_factor | 0.8154 |
| gross_win_rate | 0.4489 |
| sharpe_ratio | -7.2465 |
| sortino_ratio | -2.6394 |
| max_drawdown | 0.9653 |
| cagr | -0.7313 |
| net_avg_win | 25.4173 |
| net_avg_loss | -44.1232 |
| avg_hold_time_bars | 5.0661 |
| exposure | 0.1527 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
