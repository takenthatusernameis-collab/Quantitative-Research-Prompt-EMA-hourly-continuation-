# EMA Hourly Continuation — TIA/USDT P21_100

**Symbol:** TIA/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 423 |
| net_profit_factor | 0.9120 |
| net_win_rate | 0.5201 |
| gross_profit_factor | 1.0746 |
| gross_win_rate | 0.5201 |
| sharpe_ratio | -0.5499 |
| sortino_ratio | -0.1627 |
| max_drawdown | 0.2484 |
| cagr | -0.0768 |
| net_avg_win | 85.6440 |
| net_avg_loss | -101.7677 |
| avg_hold_time_bars | 21.7163 |
| exposure | 0.4175 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
