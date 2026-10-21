# EMA Hourly Continuation — MANA/USDT P144_200

**Symbol:** MANA/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 223 |
| net_profit_factor | 0.8524 |
| net_win_rate | 0.5471 |
| gross_profit_factor | 1.1944 |
| gross_win_rate | 0.5471 |
| sharpe_ratio | -0.6834 |
| sortino_ratio | -0.1480 |
| max_drawdown | 0.1820 |
| cagr | -0.0669 |
| net_avg_win | 75.5488 |
| net_avg_loss | -107.0575 |
| avg_hold_time_bars | 7.5785 |
| exposure | 0.0768 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
