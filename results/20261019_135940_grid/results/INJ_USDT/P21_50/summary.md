# EMA Hourly Continuation — INJ/USDT P21_50

**Symbol:** INJ/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 981 |
| net_profit_factor | 0.5692 |
| net_win_rate | 0.4822 |
| gross_profit_factor | 0.9591 |
| gross_win_rate | 0.4852 |
| sharpe_ratio | -5.7921 |
| sortino_ratio | -2.5528 |
| max_drawdown | 0.9566 |
| cagr | -0.7113 |
| net_avg_win | 26.7047 |
| net_avg_loss | -43.6805 |
| avg_hold_time_bars | 4.3670 |
| exposure | 0.1947 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
