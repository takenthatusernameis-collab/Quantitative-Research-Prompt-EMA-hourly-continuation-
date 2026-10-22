# EMA Hourly Continuation — BLZ/USDT P50_55

**Symbol:** BLZ/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 875 |
| net_profit_factor | 0.2174 |
| net_win_rate | 0.2971 |
| gross_profit_factor | 0.7283 |
| gross_win_rate | 0.3646 |
| sharpe_ratio | -13.8687 |
| sortino_ratio | -6.0450 |
| max_drawdown | 0.9997 |
| cagr | -0.9606 |
| net_avg_win | 10.6833 |
| net_avg_loss | -20.7720 |
| avg_hold_time_bars | 2.9931 |
| exposure | 0.1185 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
