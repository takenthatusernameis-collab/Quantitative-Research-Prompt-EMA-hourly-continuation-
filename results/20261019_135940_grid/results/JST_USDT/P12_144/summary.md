# EMA Hourly Continuation — JST/USDT P12_144

**Symbol:** JST/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 410 |
| net_profit_factor | 0.4712 |
| net_win_rate | 0.4805 |
| gross_profit_factor | 0.9504 |
| gross_win_rate | 0.5073 |
| sharpe_ratio | -3.8117 |
| sortino_ratio | -1.0547 |
| max_drawdown | 0.7642 |
| cagr | -0.4233 |
| net_avg_win | 33.9474 |
| net_avg_loss | -66.6361 |
| avg_hold_time_bars | 37.4585 |
| exposure | 0.6950 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
