# EMA Hourly Continuation — SLP/USDT P20_21

**Symbol:** SLP/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1390 |
| net_profit_factor | 0.1434 |
| net_win_rate | 0.2885 |
| gross_profit_factor | 0.6290 |
| gross_win_rate | 0.3647 |
| sharpe_ratio | -19.3092 |
| sortino_ratio | -10.9281 |
| max_drawdown | 1.0000 |
| cagr | -0.9978 |
| net_avg_win | 4.1735 |
| net_avg_loss | -11.8034 |
| avg_hold_time_bars | 1.8770 |
| exposure | 0.1186 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
