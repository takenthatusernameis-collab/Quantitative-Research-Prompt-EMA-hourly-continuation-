# EMA Hourly Continuation — TIA/USDT P12_20

**Symbol:** TIA/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 248 |
| net_profit_factor | 0.7618 |
| net_win_rate | 0.5040 |
| gross_profit_factor | 0.9966 |
| gross_win_rate | 0.5040 |
| sharpe_ratio | -1.2651 |
| sortino_ratio | -0.2861 |
| max_drawdown | 0.3496 |
| cagr | -0.1234 |
| net_avg_win | 72.0563 |
| net_avg_loss | -96.1200 |
| avg_hold_time_bars | 4.6048 |
| exposure | 0.0519 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
