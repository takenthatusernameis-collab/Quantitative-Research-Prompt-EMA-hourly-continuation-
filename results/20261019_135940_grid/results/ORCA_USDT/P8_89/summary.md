# EMA Hourly Continuation — ORCA/USDT P8_89

**Symbol:** ORCA/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 664 |
| net_profit_factor | 0.6253 |
| net_win_rate | 0.4759 |
| gross_profit_factor | 0.8899 |
| gross_win_rate | 0.4804 |
| sharpe_ratio | -3.6401 |
| sortino_ratio | -1.3129 |
| max_drawdown | 0.8158 |
| cagr | -0.4692 |
| net_avg_win | 42.0504 |
| net_avg_loss | -61.0618 |
| avg_hold_time_bars | 21.6822 |
| exposure | 0.6544 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
