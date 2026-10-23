# EMA Hourly Continuation — SATS/USDT P8_144

**Symbol:** SATS/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 501 |
| net_profit_factor | 0.5718 |
| net_win_rate | 0.4291 |
| gross_profit_factor | 0.7778 |
| gross_win_rate | 0.4291 |
| sharpe_ratio | -3.8747 |
| sortino_ratio | -1.2132 |
| max_drawdown | 0.7711 |
| cagr | -0.4372 |
| net_avg_win | 47.5307 |
| net_avg_loss | -62.4943 |
| avg_hold_time_bars | 31.3952 |
| exposure | 0.7118 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
