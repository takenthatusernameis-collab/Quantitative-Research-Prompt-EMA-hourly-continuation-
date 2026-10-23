# EMA Hourly Continuation — AMP/USDT P26_34

**Symbol:** AMP/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1483 |
| net_profit_factor | 0.1884 |
| net_win_rate | 0.3014 |
| gross_profit_factor | 0.6299 |
| gross_win_rate | 0.3574 |
| sharpe_ratio | -18.6638 |
| sortino_ratio | -10.5890 |
| max_drawdown | 1.0000 |
| cagr | -0.9967 |
| net_avg_win | 5.1943 |
| net_avg_loss | -11.8937 |
| avg_hold_time_bars | 2.2057 |
| exposure | 0.1487 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
