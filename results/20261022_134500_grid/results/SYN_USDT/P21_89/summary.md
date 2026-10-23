# EMA Hourly Continuation — SYN/USDT P21_89

**Symbol:** SYN/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 693 |
| net_profit_factor | 0.6646 |
| net_win_rate | 0.4791 |
| gross_profit_factor | 0.9635 |
| gross_win_rate | 0.4892 |
| sharpe_ratio | -3.4994 |
| sortino_ratio | -1.3014 |
| max_drawdown | 0.8013 |
| cagr | -0.4618 |
| net_avg_win | 47.0968 |
| net_avg_loss | -65.1694 |
| avg_hold_time_bars | 12.3304 |
| exposure | 0.3884 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
