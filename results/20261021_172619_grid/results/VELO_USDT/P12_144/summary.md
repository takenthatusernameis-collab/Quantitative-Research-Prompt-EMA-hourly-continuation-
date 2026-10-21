# EMA Hourly Continuation — VELO/USDT P12_144

**Symbol:** VELO/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 450 |
| net_profit_factor | 0.9230 |
| net_win_rate | 0.5200 |
| gross_profit_factor | 1.0635 |
| gross_win_rate | 0.5200 |
| sharpe_ratio | -0.4512 |
| sortino_ratio | -0.1376 |
| max_drawdown | 0.3312 |
| cagr | -0.0670 |
| net_avg_win | 81.8728 |
| net_avg_loss | -96.0964 |
| avg_hold_time_bars | 29.5956 |
| exposure | 0.6054 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
