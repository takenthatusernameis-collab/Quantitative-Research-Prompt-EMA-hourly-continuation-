# EMA Hourly Continuation — XEC/USDT P20_34

**Symbol:** XEC/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1233 |
| net_profit_factor | 0.3515 |
| net_win_rate | 0.4161 |
| gross_profit_factor | 0.8861 |
| gross_win_rate | 0.4615 |
| sharpe_ratio | -11.6316 |
| sortino_ratio | -5.8415 |
| max_drawdown | 0.9994 |
| cagr | -0.9477 |
| net_avg_win | 10.5588 |
| net_avg_loss | -21.4039 |
| avg_hold_time_bars | 3.1119 |
| exposure | 0.1736 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
