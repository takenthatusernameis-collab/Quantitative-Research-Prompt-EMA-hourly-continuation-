# EMA Hourly Continuation — STRAX/USDT P50_144

**Symbol:** STRAX/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 567 |
| net_profit_factor | 0.5517 |
| net_win_rate | 0.4321 |
| gross_profit_factor | 0.8715 |
| gross_win_rate | 0.4409 |
| sharpe_ratio | -5.5323 |
| sortino_ratio | -1.8699 |
| max_drawdown | 0.8929 |
| cagr | -0.5902 |
| net_avg_win | 44.8144 |
| net_avg_loss | -61.8050 |
| avg_hold_time_bars | 10.8519 |
| exposure | 0.2813 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
