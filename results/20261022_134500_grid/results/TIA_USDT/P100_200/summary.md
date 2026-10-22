# EMA Hourly Continuation — TIA/USDT P100_200

**Symbol:** TIA/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 354 |
| net_profit_factor | 0.6739 |
| net_win_rate | 0.4887 |
| gross_profit_factor | 0.9839 |
| gross_win_rate | 0.4944 |
| sharpe_ratio | -2.4583 |
| sortino_ratio | -0.6553 |
| max_drawdown | 0.5657 |
| cagr | -0.2646 |
| net_avg_win | 64.2479 |
| net_avg_loss | -91.1205 |
| avg_hold_time_bars | 9.3588 |
| exposure | 0.1506 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
