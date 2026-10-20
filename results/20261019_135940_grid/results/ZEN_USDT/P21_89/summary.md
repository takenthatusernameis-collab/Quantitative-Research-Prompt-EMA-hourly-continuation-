# EMA Hourly Continuation — ZEN/USDT P21_89

**Symbol:** ZEN/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 747 |
| net_profit_factor | 0.5786 |
| net_win_rate | 0.4565 |
| gross_profit_factor | 0.8759 |
| gross_win_rate | 0.4659 |
| sharpe_ratio | -4.8312 |
| sortino_ratio | -1.8561 |
| max_drawdown | 0.8975 |
| cagr | -0.5905 |
| net_avg_win | 35.9908 |
| net_avg_loss | -52.2430 |
| avg_hold_time_bars | 11.1861 |
| exposure | 0.3798 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
