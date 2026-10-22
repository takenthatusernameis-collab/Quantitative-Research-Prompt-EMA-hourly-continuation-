# EMA Hourly Continuation — AGLD/USDT P12_89

**Symbol:** AGLD/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 567 |
| net_profit_factor | 0.7984 |
| net_win_rate | 0.4921 |
| gross_profit_factor | 0.9883 |
| gross_win_rate | 0.4921 |
| sharpe_ratio | -1.8812 |
| sortino_ratio | -0.6384 |
| max_drawdown | 0.5815 |
| cagr | -0.2556 |
| net_avg_win | 74.5447 |
| net_avg_loss | -90.4467 |
| avg_hold_time_bars | 21.2416 |
| exposure | 0.5451 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
