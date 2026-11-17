# EMA Hourly Continuation — NUM/USDT P89_100

**Symbol:** NUM/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 567 |
| net_profit_factor | 0.2819 |
| net_win_rate | 0.3333 |
| gross_profit_factor | 0.8122 |
| gross_win_rate | 0.3633 |
| sharpe_ratio | -9.6299 |
| sortino_ratio | -3.3166 |
| max_drawdown | 0.9866 |
| cagr | -0.8193 |
| net_avg_win | 20.4917 |
| net_avg_loss | -36.3406 |
| avg_hold_time_bars | 4.1817 |
| exposure | 0.1078 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
