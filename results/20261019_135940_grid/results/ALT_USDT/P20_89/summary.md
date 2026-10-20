# EMA Hourly Continuation — ALT/USDT P20_89

**Symbol:** ALT/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 656 |
| net_profit_factor | 0.6145 |
| net_win_rate | 0.4619 |
| gross_profit_factor | 0.8727 |
| gross_win_rate | 0.4680 |
| sharpe_ratio | -3.8098 |
| sortino_ratio | -1.3780 |
| max_drawdown | 0.8122 |
| cagr | -0.4767 |
| net_avg_win | 42.2647 |
| net_avg_loss | -59.0353 |
| avg_hold_time_bars | 13.2302 |
| exposure | 0.3945 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
