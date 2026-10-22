# EMA Hourly Continuation — XTZ/USDT P55_89

**Symbol:** XTZ/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 741 |
| net_profit_factor | 0.4101 |
| net_win_rate | 0.4494 |
| gross_profit_factor | 0.9308 |
| gross_win_rate | 0.4831 |
| sharpe_ratio | -6.9852 |
| sortino_ratio | -2.7113 |
| max_drawdown | 0.9636 |
| cagr | -0.7301 |
| net_avg_win | 20.0970 |
| net_avg_loss | -39.9985 |
| avg_hold_time_bars | 4.1066 |
| exposure | 0.1383 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
