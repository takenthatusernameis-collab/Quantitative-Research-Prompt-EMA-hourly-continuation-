# EMA Hourly Continuation — APT/USDT P21_34

**Symbol:** APT/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 259 |
| net_profit_factor | 0.6284 |
| net_win_rate | 0.4710 |
| gross_profit_factor | 0.8670 |
| gross_win_rate | 0.4710 |
| sharpe_ratio | -2.1954 |
| sortino_ratio | -0.5052 |
| max_drawdown | 0.4665 |
| cagr | -0.2062 |
| net_avg_win | 61.0009 |
| net_avg_loss | -86.4407 |
| avg_hold_time_bars | 5.7915 |
| exposure | 0.0682 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
