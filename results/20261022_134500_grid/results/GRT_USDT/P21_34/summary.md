# EMA Hourly Continuation — GRT/USDT P21_34

**Symbol:** GRT/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1113 |
| net_profit_factor | 0.3677 |
| net_win_rate | 0.4043 |
| gross_profit_factor | 0.7828 |
| gross_win_rate | 0.4304 |
| sharpe_ratio | -11.0290 |
| sortino_ratio | -5.2229 |
| max_drawdown | 0.9988 |
| cagr | -0.9306 |
| net_avg_win | 12.9073 |
| net_avg_loss | -23.8255 |
| avg_hold_time_bars | 2.4483 |
| exposure | 0.1233 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
