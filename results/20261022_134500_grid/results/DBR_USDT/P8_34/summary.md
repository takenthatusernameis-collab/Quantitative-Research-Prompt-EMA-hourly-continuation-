# EMA Hourly Continuation — DBR/USDT P8_34

**Symbol:** DBR/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 874 |
| net_profit_factor | 0.5680 |
| net_win_rate | 0.4645 |
| gross_profit_factor | 1.0570 |
| gross_win_rate | 0.4874 |
| sharpe_ratio | -7.2543 |
| sortino_ratio | -3.3665 |
| max_drawdown | 0.9660 |
| cagr | -0.8084 |
| net_avg_win | 31.2073 |
| net_avg_loss | -47.6657 |
| avg_hold_time_bars | 7.3272 |
| exposure | 0.3642 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
