# EMA Hourly Continuation — TNSR/USDT P20_50

**Symbol:** TNSR/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 938 |
| net_profit_factor | 0.6672 |
| net_win_rate | 0.4872 |
| gross_profit_factor | 1.0437 |
| gross_win_rate | 0.5021 |
| sharpe_ratio | -4.8645 |
| sortino_ratio | -2.0934 |
| max_drawdown | 0.9268 |
| cagr | -0.6338 |
| net_avg_win | 40.3925 |
| net_avg_loss | -57.5179 |
| avg_hold_time_bars | 5.4264 |
| exposure | 0.2303 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
