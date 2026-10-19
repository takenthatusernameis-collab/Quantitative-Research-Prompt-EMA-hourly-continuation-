# EMA Hourly Continuation — BAT/USDT P12_89

**Symbol:** BAT/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 722 |
| net_profit_factor | 0.6053 |
| net_win_rate | 0.4765 |
| gross_profit_factor | 0.9741 |
| gross_win_rate | 0.4861 |
| sharpe_ratio | -4.2300 |
| sortino_ratio | -1.5908 |
| max_drawdown | 0.8680 |
| cagr | -0.5373 |
| net_avg_win | 38.1454 |
| net_avg_loss | -57.3497 |
| avg_hold_time_bars | 16.3698 |
| exposure | 0.5372 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
