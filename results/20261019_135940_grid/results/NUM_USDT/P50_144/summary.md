# EMA Hourly Continuation — NUM/USDT P50_144

**Symbol:** NUM/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 522 |
| net_profit_factor | 0.5700 |
| net_win_rate | 0.4157 |
| gross_profit_factor | 0.8112 |
| gross_win_rate | 0.4234 |
| sharpe_ratio | -4.6345 |
| sortino_ratio | -1.4890 |
| max_drawdown | 0.8467 |
| cagr | -0.5062 |
| net_avg_win | 50.7089 |
| net_avg_loss | -63.2908 |
| avg_hold_time_bars | 13.8582 |
| exposure | 0.3288 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
