# EMA Hourly Continuation — CKB/USDT P12_26

**Symbol:** CKB/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1400 |
| net_profit_factor | 0.4161 |
| net_win_rate | 0.4186 |
| gross_profit_factor | 0.8055 |
| gross_win_rate | 0.4486 |
| sharpe_ratio | -11.0344 |
| sortino_ratio | -5.8308 |
| max_drawdown | 0.9993 |
| cagr | -0.9455 |
| net_avg_win | 12.1540 |
| net_avg_loss | -21.0265 |
| avg_hold_time_bars | 3.0093 |
| exposure | 0.1915 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
