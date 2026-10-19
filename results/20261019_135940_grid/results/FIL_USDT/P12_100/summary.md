# EMA Hourly Continuation — FIL/USDT P12_100

**Symbol:** FIL/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 624 |
| net_profit_factor | 0.6153 |
| net_win_rate | 0.4631 |
| gross_profit_factor | 0.9313 |
| gross_win_rate | 0.4744 |
| sharpe_ratio | -3.9698 |
| sortino_ratio | -1.3973 |
| max_drawdown | 0.8201 |
| cagr | -0.4847 |
| net_avg_win | 44.8693 |
| net_avg_loss | -62.9126 |
| avg_hold_time_bars | 20.9151 |
| exposure | 0.5932 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
