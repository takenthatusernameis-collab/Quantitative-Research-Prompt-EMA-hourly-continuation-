# EMA Hourly Continuation — CETUS/USDT P20_100

**Symbol:** CETUS/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 498 |
| net_profit_factor | 0.8774 |
| net_win_rate | 0.5161 |
| gross_profit_factor | 1.0680 |
| gross_win_rate | 0.5161 |
| sharpe_ratio | -0.9718 |
| sortino_ratio | -0.3107 |
| max_drawdown | 0.3789 |
| cagr | -0.1373 |
| net_avg_win | 86.6309 |
| net_avg_loss | -105.2853 |
| avg_hold_time_bars | 18.5361 |
| exposure | 0.4177 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
