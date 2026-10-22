# EMA Hourly Continuation — MANTA/USDT P12_21

**Symbol:** MANTA/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 402 |
| net_profit_factor | 0.7448 |
| net_win_rate | 0.5025 |
| gross_profit_factor | 1.0512 |
| gross_win_rate | 0.5025 |
| sharpe_ratio | -2.2271 |
| sortino_ratio | -0.6410 |
| max_drawdown | 0.5762 |
| cagr | -0.2544 |
| net_avg_win | 75.3577 |
| net_avg_loss | -102.1882 |
| avg_hold_time_bars | 5.3060 |
| exposure | 0.0970 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
