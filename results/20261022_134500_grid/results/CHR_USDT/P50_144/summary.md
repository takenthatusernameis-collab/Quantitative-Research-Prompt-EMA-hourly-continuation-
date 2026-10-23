# EMA Hourly Continuation — CHR/USDT P50_144

**Symbol:** CHR/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 522 |
| net_profit_factor | 0.6527 |
| net_win_rate | 0.4770 |
| gross_profit_factor | 0.9311 |
| gross_win_rate | 0.4808 |
| sharpe_ratio | -3.1377 |
| sortino_ratio | -1.0108 |
| max_drawdown | 0.7224 |
| cagr | -0.3794 |
| net_avg_win | 52.8117 |
| net_avg_loss | -73.8038 |
| avg_hold_time_bars | 13.1935 |
| exposure | 0.3116 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
