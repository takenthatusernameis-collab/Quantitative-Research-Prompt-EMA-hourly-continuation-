# EMA Hourly Continuation — MANTA/USDT P55_89

**Symbol:** MANTA/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 328 |
| net_profit_factor | 0.6112 |
| net_win_rate | 0.4512 |
| gross_profit_factor | 0.8222 |
| gross_win_rate | 0.4512 |
| sharpe_ratio | -2.8736 |
| sortino_ratio | -0.7416 |
| max_drawdown | 0.5881 |
| cagr | -0.2889 |
| net_avg_win | 61.1029 |
| net_avg_loss | -82.2010 |
| avg_hold_time_bars | 7.6463 |
| exposure | 0.1140 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
