# EMA Hourly Continuation — SHR/USDT P55_89

**Symbol:** SHR/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 874 |
| net_profit_factor | 0.3681 |
| net_win_rate | 0.3284 |
| gross_profit_factor | 0.5852 |
| gross_win_rate | 0.3307 |
| sharpe_ratio | -9.8686 |
| sortino_ratio | -4.0945 |
| max_drawdown | 0.9937 |
| cagr | -0.8654 |
| net_avg_win | 20.1682 |
| net_avg_loss | -26.7883 |
| avg_hold_time_bars | 3.7746 |
| exposure | 0.1493 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
