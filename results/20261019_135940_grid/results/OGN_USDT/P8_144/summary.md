# EMA Hourly Continuation — OGN/USDT P8_144

**Symbol:** OGN/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 469 |
| net_profit_factor | 0.5310 |
| net_win_rate | 0.4179 |
| gross_profit_factor | 0.7856 |
| gross_win_rate | 0.4350 |
| sharpe_ratio | -4.4428 |
| sortino_ratio | -1.3449 |
| max_drawdown | 0.8115 |
| cagr | -0.4750 |
| net_avg_win | 46.3934 |
| net_avg_loss | -62.7275 |
| avg_hold_time_bars | 35.8230 |
| exposure | 0.7603 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
