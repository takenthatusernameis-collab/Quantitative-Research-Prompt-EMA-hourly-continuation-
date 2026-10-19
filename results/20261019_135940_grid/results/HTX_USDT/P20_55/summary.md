# EMA Hourly Continuation — HTX/USDT P20_55

**Symbol:** HTX/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1057 |
| net_profit_factor | 0.1998 |
| net_win_rate | 0.3037 |
| gross_profit_factor | 0.6346 |
| gross_win_rate | 0.3746 |
| sharpe_ratio | -15.6676 |
| sortino_ratio | -7.5819 |
| max_drawdown | 1.0000 |
| cagr | -0.9843 |
| net_avg_win | 7.7772 |
| net_avg_loss | -16.9785 |
| avg_hold_time_bars | 6.1911 |
| exposure | 0.2961 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
