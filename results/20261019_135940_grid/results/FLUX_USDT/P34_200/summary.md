# EMA Hourly Continuation — FLUX/USDT P34_200

**Symbol:** FLUX/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 377 |
| net_profit_factor | 0.6685 |
| net_win_rate | 0.4828 |
| gross_profit_factor | 0.9692 |
| gross_win_rate | 0.4934 |
| sharpe_ratio | -2.3939 |
| sortino_ratio | -0.6544 |
| max_drawdown | 0.5774 |
| cagr | -0.2682 |
| net_avg_win | 60.2309 |
| net_avg_loss | -84.0874 |
| avg_hold_time_bars | 29.1857 |
| exposure | 0.5001 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
