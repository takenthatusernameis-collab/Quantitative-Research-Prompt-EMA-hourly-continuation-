# EMA Hourly Continuation — ARB/USDT P12_89

**Symbol:** ARB/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 665 |
| net_profit_factor | 0.5997 |
| net_win_rate | 0.4872 |
| gross_profit_factor | 0.9648 |
| gross_win_rate | 0.4932 |
| sharpe_ratio | -3.9006 |
| sortino_ratio | -1.3994 |
| max_drawdown | 0.8269 |
| cagr | -0.4990 |
| net_avg_win | 38.0873 |
| net_avg_loss | -60.3447 |
| avg_hold_time_bars | 18.3278 |
| exposure | 0.5540 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
