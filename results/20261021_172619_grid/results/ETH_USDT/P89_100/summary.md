# EMA Hourly Continuation — ETH/USDT P89_100

**Symbol:** ETH/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 80 |
| net_profit_factor | 0.5356 |
| net_win_rate | 0.4750 |
| gross_profit_factor | 0.8712 |
| gross_win_rate | 0.4750 |
| sharpe_ratio | -1.5880 |
| sortino_ratio | -0.2044 |
| max_drawdown | 0.2628 |
| cagr | -0.0888 |
| net_avg_win | 63.2008 |
| net_avg_loss | -106.7619 |
| avg_hold_time_bars | 5.8250 |
| exposure | 0.0212 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
