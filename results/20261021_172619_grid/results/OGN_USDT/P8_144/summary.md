# EMA Hourly Continuation — OGN/USDT P8_144

**Symbol:** OGN/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 368 |
| net_profit_factor | 0.6212 |
| net_win_rate | 0.4321 |
| gross_profit_factor | 0.7631 |
| gross_win_rate | 0.4321 |
| sharpe_ratio | -2.9207 |
| sortino_ratio | -0.7886 |
| max_drawdown | 0.6266 |
| cagr | -0.3071 |
| net_avg_win | 62.2778 |
| net_avg_loss | -76.2647 |
| avg_hold_time_bars | 45.1603 |
| exposure | 0.7520 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
