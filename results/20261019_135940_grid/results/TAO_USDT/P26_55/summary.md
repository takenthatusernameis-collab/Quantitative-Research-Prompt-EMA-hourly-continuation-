# EMA Hourly Continuation — TAO/USDT P26_55

**Symbol:** TAO/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 932 |
| net_profit_factor | 0.5887 |
| net_win_rate | 0.4764 |
| gross_profit_factor | 0.9490 |
| gross_win_rate | 0.4850 |
| sharpe_ratio | -5.7763 |
| sortino_ratio | -2.4673 |
| max_drawdown | 0.9537 |
| cagr | -0.7021 |
| net_avg_win | 30.6910 |
| net_avg_loss | -47.4361 |
| avg_hold_time_bars | 3.9002 |
| exposure | 0.1652 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
