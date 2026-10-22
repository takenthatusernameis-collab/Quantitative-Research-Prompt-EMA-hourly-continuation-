# EMA Hourly Continuation — BOSON/USDT P20_89

**Symbol:** BOSON/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 719 |
| net_profit_factor | 0.6695 |
| net_win_rate | 0.4618 |
| gross_profit_factor | 0.9352 |
| gross_win_rate | 0.4687 |
| sharpe_ratio | -3.7784 |
| sortino_ratio | -1.4261 |
| max_drawdown | 0.8154 |
| cagr | -0.4889 |
| net_avg_win | 49.7053 |
| net_avg_loss | -63.6920 |
| avg_hold_time_bars | 11.7274 |
| exposure | 0.3833 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
