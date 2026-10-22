# EMA Hourly Continuation — KNC/USDT P12_34

**Symbol:** KNC/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 731 |
| net_profit_factor | 0.5946 |
| net_win_rate | 0.4528 |
| gross_profit_factor | 0.8850 |
| gross_win_rate | 0.4542 |
| sharpe_ratio | -5.1226 |
| sortino_ratio | -1.9791 |
| max_drawdown | 0.9054 |
| cagr | -0.5988 |
| net_avg_win | 39.8443 |
| net_avg_loss | -55.4488 |
| avg_hold_time_bars | 8.5007 |
| exposure | 0.2825 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
