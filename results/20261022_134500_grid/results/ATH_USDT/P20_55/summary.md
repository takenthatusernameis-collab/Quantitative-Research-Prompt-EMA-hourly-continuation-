# EMA Hourly Continuation — ATH/USDT P20_55

**Symbol:** ATH/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 867 |
| net_profit_factor | 0.5934 |
| net_win_rate | 0.4787 |
| gross_profit_factor | 0.9423 |
| gross_win_rate | 0.4810 |
| sharpe_ratio | -5.1777 |
| sortino_ratio | -2.2304 |
| max_drawdown | 0.9211 |
| cagr | -0.6540 |
| net_avg_win | 32.2759 |
| net_avg_loss | -49.9401 |
| avg_hold_time_bars | 5.8697 |
| exposure | 0.2467 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
