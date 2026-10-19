# EMA Hourly Continuation — ARB/USDT P12_34

**Symbol:** ARB/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1259 |
| net_profit_factor | 0.4360 |
| net_win_rate | 0.4782 |
| gross_profit_factor | 0.9091 |
| gross_win_rate | 0.4885 |
| sharpe_ratio | -7.5525 |
| sortino_ratio | -3.7631 |
| max_drawdown | 0.9909 |
| cagr | -0.8430 |
| net_avg_win | 12.7203 |
| net_avg_loss | -26.7306 |
| avg_hold_time_bars | 3.9087 |
| exposure | 0.2237 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
