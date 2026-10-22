# EMA Hourly Continuation — HTX/USDT P55_89

**Symbol:** HTX/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 792 |
| net_profit_factor | 0.1878 |
| net_win_rate | 0.2588 |
| gross_profit_factor | 0.5925 |
| gross_win_rate | 0.3422 |
| sharpe_ratio | -14.8243 |
| sortino_ratio | -6.3797 |
| max_drawdown | 0.9998 |
| cagr | -0.9686 |
| net_avg_win | 11.2785 |
| net_avg_loss | -20.9718 |
| avg_hold_time_bars | 4.6427 |
| exposure | 0.1664 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
