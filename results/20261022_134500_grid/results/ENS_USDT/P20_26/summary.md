# EMA Hourly Continuation — ENS/USDT P20_26

**Symbol:** ENS/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1257 |
| net_profit_factor | 0.2681 |
| net_win_rate | 0.3548 |
| gross_profit_factor | 0.6853 |
| gross_win_rate | 0.4010 |
| sharpe_ratio | -14.9230 |
| sortino_ratio | -7.6736 |
| max_drawdown | 1.0000 |
| cagr | -0.9841 |
| net_avg_win | 8.2112 |
| net_avg_loss | -16.8458 |
| avg_hold_time_bars | 2.0263 |
| exposure | 0.1158 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
