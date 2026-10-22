# EMA Hourly Continuation — CRV/USDT P50_100

**Symbol:** CRV/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 673 |
| net_profit_factor | 0.5339 |
| net_win_rate | 0.4681 |
| gross_profit_factor | 0.9040 |
| gross_win_rate | 0.4770 |
| sharpe_ratio | -5.0426 |
| sortino_ratio | -1.8479 |
| max_drawdown | 0.8988 |
| cagr | -0.5903 |
| net_avg_win | 32.5000 |
| net_avg_loss | -53.5583 |
| avg_hold_time_bars | 5.1872 |
| exposure | 0.1587 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
