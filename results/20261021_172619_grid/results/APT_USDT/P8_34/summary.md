# EMA Hourly Continuation — APT/USDT P8_34

**Symbol:** APT/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 670 |
| net_profit_factor | 0.6963 |
| net_win_rate | 0.4776 |
| gross_profit_factor | 0.9045 |
| gross_win_rate | 0.4776 |
| sharpe_ratio | -2.8854 |
| sortino_ratio | -1.0664 |
| max_drawdown | 0.7097 |
| cagr | -0.3865 |
| net_avg_win | 50.6341 |
| net_avg_loss | -66.4901 |
| avg_hold_time_bars | 9.1955 |
| exposure | 0.2800 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
