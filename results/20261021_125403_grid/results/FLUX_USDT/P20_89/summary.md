# EMA Hourly Continuation — FLUX/USDT P20_89

**Symbol:** FLUX/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 519 |
| net_profit_factor | 0.8821 |
| net_win_rate | 0.5279 |
| gross_profit_factor | 1.1106 |
| gross_win_rate | 0.5279 |
| sharpe_ratio | -0.8340 |
| sortino_ratio | -0.2741 |
| max_drawdown | 0.3167 |
| cagr | -0.1222 |
| net_avg_win | 76.1821 |
| net_avg_loss | -96.5924 |
| avg_hold_time_bars | 15.5029 |
| exposure | 0.3657 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
