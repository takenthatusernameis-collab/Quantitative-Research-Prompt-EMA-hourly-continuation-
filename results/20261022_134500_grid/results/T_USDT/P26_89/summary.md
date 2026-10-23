# EMA Hourly Continuation — T/USDT P26_89

**Symbol:** T/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 618 |
| net_profit_factor | 0.5569 |
| net_win_rate | 0.4595 |
| gross_profit_factor | 0.9208 |
| gross_win_rate | 0.4676 |
| sharpe_ratio | -5.0641 |
| sortino_ratio | -1.7554 |
| max_drawdown | 0.8899 |
| cagr | -0.5803 |
| net_avg_win | 39.3097 |
| net_avg_loss | -60.0154 |
| avg_hold_time_bars | 11.2832 |
| exposure | 0.3155 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
