# EMA Hourly Continuation — TFUEL/USDT P55_89

**Symbol:** TFUEL/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 767 |
| net_profit_factor | 0.3823 |
| net_win_rate | 0.3794 |
| gross_profit_factor | 0.7686 |
| gross_win_rate | 0.4029 |
| sharpe_ratio | -9.3618 |
| sortino_ratio | -3.6900 |
| max_drawdown | 0.9905 |
| cagr | -0.8411 |
| net_avg_win | 21.0594 |
| net_avg_loss | -33.6802 |
| avg_hold_time_bars | 4.1121 |
| exposure | 0.1427 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
